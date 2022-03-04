from PIL import ImageColor


def arrange(item , dim, min, max):
    item_count,i=len(item),0
    for i in range(dim):
        if(i<= item_count):
            item[i]= item[i]/((max-min)/100)
        else:
            item[i]= 50/((max-min)/100)
    return item

def kokal(x):
    return x**(1/2)

def usal(x,level):
    return x**(level)

def vectorBenzerlik(A,B):
    if len(A) != len(B):
        return -1
    else:
        len_ = len(A)
        total=0
        for i in range(len_):
            total += usal((B[i]-A[i]),2)
            distance = kokal(total)
            max_dist=0
        for i in range(len_):
            max_dist += usal(100,2)
        max_dist = kokal(max_dist)

        return 1-(distance/max_dist)
    return 0

kirmizi=[255,0,0]
koyuKirmizi=[181,25,25]
kahverengi=[48,34,15]
siyah=[0,0,0]
beyaz=[255,255,255]
gri=[82,82,82]

kirmizi_normalized = arrange(kirmizi,3,0,255)
koyuKirmizi_normalized = arrange(koyuKirmizi,3,0,255)
kahverengi_normalized = arrange(kahverengi,3,0,255)
siyah_normalized = arrange(siyah,3,0,255)
beyaz_normalized = arrange(beyaz,3,0,255)
gri_normalized = arrange(gri,3,0,255)
benzerlikOranı = vectorBenzerlik(kirmizi_normalized,koyuKirmizi_normalized)

def hex_to_rgb():
    color_list=[]
    f = open("color.txt","r")
    for i in f.readlines():
        if i.endswith(",\n"):
            i=i[:-2]
        s=eval(i)
        color_list.append(s)
    for j in color_list:
        j[0]=ImageColor.getcolor(f"#{j[0]}", "RGB")
        j[0]=list(j[0])
        j[0]=arrange(j[0],3,0,255)
    return color_list

def benzer_bul(A):
    en_yuksek_benzerlik=0
    en_benzer= "Yok"
    for i in hex_to_rgb():
        if A == i[0]:
            continue
        sim = vectorBenzerlik(A,i[0])

        if sim > en_yuksek_benzerlik:
            en_yuksek_benzerlik = sim
            en_benzer= i[1]
    return en_benzer

if __name__ == "__main__":
    renk = input("Renginizin Hex Kodunu giriniz: ")
    renk_normalized = arrange(list(ImageColor.getcolor(renk,"RGB")),3,0,255)
    print(benzer_bul(renk_normalized))
