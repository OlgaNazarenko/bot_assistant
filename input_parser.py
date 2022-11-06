import inspect
from utils import input_error
from types import FunctionType
from constants import COMMANDS


@input_error
def search_args(data: str) -> tuple[FunctionType, list[str] | None]:
    for command, func in COMMANDS.items():

        if data.lower().startswith(command):
            args = data[len(command):].strip().split(' ')

            if check_args(func, args):
                return func, args

            return func, None
    else:
        raise ValueError("You entered an unknown command. Please enter the required command.\n")


def check_args(func, args: list) -> bool:
    func_params = inspect.getfullargspec(func.__dict__['__wrapped__'])  #??????

    if not func_params.args:
        return False

    if len(func_params.args) == len(args) and args[0]:
        return True
    elif len(args) >= (len(func_params.args)-len(func_params.defaults)) <= len(args):
        return True

    elif len(args) > len(func_params.args):
        all_args = ' '.join(func_params.args)
        raise ValueError(f"More arguments are listed than the command can accept. "
                         f"\nArguments command: <{all_args}>")

    required_args = ' '.join(func_params.args[:len(func_params.defaults)] if
                             func_params.defaults else func_params.args)

    raise ValueError(f"Not all mandatory command arguments are listed: <{required_args}>\n")
