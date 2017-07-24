#!/usr/bin/python3
"""Quick purge of all docker containers, volumes, images
BJP 7/1/17"""

from subprocess import call
import argparse

def Main():
    """ Main()"""
    parser = argparse.ArgumentParser()
    parser.add_argument("DockertypeToPurge", type=str, help="purge all items in a "
                        "particular docker type: images, containers, volumes")
    parser.add_argument("-y", "--yes", action="store_true", help="suppress "
                        "confirmation (quiet mode)")
    args = parser.parse_args()
    dockerTypeToPurge = args.DockertypeToPurge.lstrip()

    try:
        # python switch/case "ish"
        if dockerTypeToPurge == "images":
            if args.yes:
                DisplayAction(dockerTypeToPurge)
                call("docker rmi $(docker images -q)")
            else:
                answer = input(PromptQuestion(dockerTypeToPurge))
                answer = True if answer.lstrip() == 'yes' else False
                if answer:
                    DisplayAction(dockerTypeToPurge)
                    call("docker rmi $(docker images -q)")
        elif dockerTypeToPurge == "containers":
            if args.yes:
                DisplayAction(dockerTypeToPurge)
                call("docker rm $(docker ps -aq)")
            else:
                answer = input(PromptQuestion(dockerTypeToPurge))
                answer = True if answer.lstrip() == 'yes' else False
                if answer:
                    DisplayAction(dockerTypeToPurge)
                    call("docker rm $(docker ps -aq)")
        elif dockerTypeToPurge == "volumes":
            if args.yes:
                DisplayAction(dockerTypeToPurge)
                call("docker volume rm $(docker volume ls -q)")
            else:
                answer = input(PromptQuestion(dockerTypeToPurge))
                answer = True if answer.lstrip() == 'yes' else False
                if answer:
                    DisplayAction(dockerTypeToPurge)
                    call("docker volume rm $(docker volume ls -q)")
        elif dockerTypeToPurge == "testcase":
            if args.yes:
                DisplayAction(dockerTypeToPurge)
                call("docker ps -a")
            else:
                answer = input("Are you sure you wish to display running "
                               "containers '{0}': ".format(dockerTypeToPurge))
                answer = True if answer.lstrip() == 'yes' else False
                if answer:
                    DisplayAction(dockerTypeToPurge)
                    call("docker ps -a")
        else:
            raise ValueError("\nYou must enter a type to purge: images, containers or volumes")
    except ValueError as ve:
        print(str(ve))
    except Exception as e:
        print("Unknown error - REASON: {0}".format(e))


def DisplayAction(dockerType):
    """ Run action info message"""
    message = "\n Purging all docker '{0}' in the environment!".format(dockerType)
    return message


def PromptQuestion(dockerType):
    """ Prompt user action """
    question = "\n Are you sure you wish to purge all {0}: ".format(dockerType)
    return question


if __name__ == '__main__':
    Main()
