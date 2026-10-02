from engine.orchestrator import EpisodeOrchestrator


def main():

    script = input(
        "\nEnter your ASHVA episode concept:\n> "
    )

    orchestrator = EpisodeOrchestrator()

    orchestrator.run(script)


if __name__ == "__main__":
    main()