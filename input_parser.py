from utils import input_error
from types import FunctionType

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
    func_params = inspect.getfullargspec(func.__dict__['__wrapped__']).args

    if not func_params:
        return False

    if len(func_params) == len(args):
        return True

    raise ValueError("Not all mandatory command arguments are listed\n")

