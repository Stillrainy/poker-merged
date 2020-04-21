from PIL import Image
import os
import random
import sys


class Poker():

    def loadFilesName(self):
        self.filesName = os.listdir('img/')
        self.length = len(self.filesName)

        for i in range(self.length):
            self.filesName[i] = 'img/' + self.filesName[i]
        return self.filesName

    def generateImg(self, width, height, numOfPokers):
        width = int(width * 94.488188976)
        height = int(height * 94.488188976)
        image = Image.new('RGBA', (width, height))

        try:
            from tqdm import tqdm
            with tqdm(total=numOfPokers, ncols=75) as pbar:
                for i in range(numOfPokers):
                    curImge = Image.open(
                        self.filesName[random.randint(0, self.length-1)]
                    )

                    rotImge = curImge.rotate(
                        random.randint(0, 360),
                        Image.NEAREST,
                        expand=1
                    )

                    image.paste(
                        rotImge,
                        (random.randint(-500, width),
                         random.randint(-500, height)),
                        rotImge
                    )

                    pbar.update(1)
        except KeyboardInterrupt:
            pbar.close()
            raise
        pbar.close()

        print('Generating...')
        image.save('output/merged.png', dpi=(240, 240))
        print(r"Output to: 'output/merged.png'")


if __name__ == '__main__':
    myPoker = Poker()
    myPoker.loadFilesName()
    myPoker.generateImg(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
