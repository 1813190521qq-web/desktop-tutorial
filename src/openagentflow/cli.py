"""Small command-line smoke entrypoint."""

from . import Agent, EchoModel, Flow, Message


def main() -> None:
    result = Flow([Agent("echo")], model=EchoModel()).run([Message.user("OpenAgentFlow is ready.")])
    print(result.output)


if __name__ == "__main__":
    main()

