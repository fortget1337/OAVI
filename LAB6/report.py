import os

if __name__ == '__main__':
    with open('./LAB6/result/README.md', 'a+') as file:
        for i in sorted(os.listdir("LAB6/pictures_results/symbols"), key=lambda x: int(x.split('.')[0])):
            file.write(f"![imgOut](../pictures_results/symbols/{i}) ")