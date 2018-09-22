import matplotlib.pyplot as plt
import utils


def mainOpera(imagem1,imagem2,operacao):
    # formato das imagens 1a e 1b são diferentes do esperado 
    ImgOriginal1 = utils.LerImagem('../Imagens/Originais/{}.png'.format(imagem1))
    ImgOriginal2 = utils.LerImagem('../Imagens/Originais/{}.png'.format(imagem2))   

    ImgResultado = utils.operation(ImgOriginal1,ImgOriginal2,operacao)

    fig, [ax1,ax2,ax3] = plt.subplots(1,3,figsize=(20,30))
    ax1.imshow(ImgOriginal1,cmap='gray')
    ax2.imshow(ImgOriginal2,cmap='gray')
    ax3.imshow(ImgResultado,cmap='gray')
    plt.show()
    
if __name__ == '__main__':
    mainOpera('Image_(1a)','Image_(1b)','xand')