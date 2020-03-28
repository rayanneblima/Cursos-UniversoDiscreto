import numpy as np
import cv2


def showImage(img):
    from matplotlib import pyplot as plt

    #opencv = bgr  ---  matplotlib = rgb
    #convertendo a cor:
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(imgMPLIB)
    plt.show()
    
def saveBlueImage(img, filename):
    altura, largura, canais = img.shape
    for y in range(0, altura):
        for x in range(0, largura):
            azul = img.item(y, x, 0)
            verde = img.item(y, x, 1)
            vermelho = img.item(y, x, 2)
    
            #print(x, y, ":", vermelho, verde, azul)
            #imagem apenas com tom azul
            img.itemset((y, x, 1), 0)
            img.itemset((y, x, 2), 0)
 
    #criando nova imagem
    cv2.imwrite(filename, img)

def saveResizedVideo(inputFile, outputFile):
    cap = cv2.VideoCapture(inputFile)

    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D') #codec de video
    out = cv2.VideoWriter(outputFile, fourcc, 20.0, (640,480))
    frames = 0
    while(cap.isOpened()):
        ret, frame = cap.read()

        if not ret or frames > 200:
            print("FINISHED")
            break

        #redimensionando um video, largura x altura
        newFrame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)
        out.write(newFrame)
        frames += 1
    cap.release()
    out.release()
    
def main():
    
    #imgOpenCV = cv2.imread("ada.jpg")
    #saveBlueImage(imgOpenCV, "adazul.jpg")
    #showImage(imgOpenCV)
    #saveResizedVideo("v.mkv", "output.avi")
    thumbnail = cv2.imread("ARTIGOS.jpg")
    logo = cv2.imread("logosvbr.png")
    logo = cv2.resize(logo, (300,300))

    thumbH, thumbW, _ = thumbnail.shape
    logoH, logoW, _ = logo.shape

    crop = thumbnail[thumbH - logoH:, thumbW - logoW:]
    logoGray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    ret, maskLogo = cv2.threshold(logoGray, 100, 255, cv2.THRESH_BINARY) #pixel abaixo de 100, ficará preto
    fundo = cv2.bitwise_and(crop, crop, mask = maskLogo) #compara ambas as imagens com AND, ignorando a maskLogo
    maskLogoInv = cv2.bitwise_not(maskLogo) #inverte as cores BINARIAS
    frente = cv2.bitwise_and(logo, logo, mask = maskLogoInv)
    imgJunta = cv2.add(frente, fundo)

    thumbnail[thumbH - logoH:, thumbW - logoW:] = imgJunta
    
    showImage(thumbnail)

    

#definir função main corretamente, verificando se o arquivo
#está sendo executado direta ou indiretamente (import de alguma função)
#codigo vira uma biblioteca
if __name__ == "__main__":
    main()



