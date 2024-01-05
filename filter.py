#### Note: the final code is online 1089. The commented codes are tests I did to develop the aplication.
## I didn't upload the source list of words on GitHub because they're too large.


############## REMOVENDO MAIUSCULAS ######################
# f = open("ukrainian stress.txt", "r", encoding="utf8")
# g = open("ukrainian stress filtrado.txt", "w", encoding="utf8")

# def checa_maiusc(word):
#     if word.startswith("А́") or word.startswith("Е́") or word.startswith("І́") or word.startswith("У́") or word.startswith("О́") or word.startswith("Є́") or word.startswith("Я́") or word.startswith("Ї́") or word.startswith("Е́") or word.startswith("Ґ") or word.startswith("Ю") or word.startswith("Б") or word.startswith("Т") or word.startswith("И") or word.startswith("М") or word.startswith("С") or word.startswith("Ч") or word.startswith("Я") or word.startswith("Є") or word.startswith("Ж") or word.startswith("Д") or word.startswith("Л") or word.startswith("О") or word.startswith("Р") or word.startswith("П") or word.startswith("А") or word.startswith("В") or word.startswith("І") or word.startswith("Ф") or word.startswith("Ї") or word.startswith("Х") or word.startswith("З") or word.startswith("Щ") or word.startswith("Ш") or word.startswith("Г") or word.startswith("Н") or word.startswith("Е") or word.startswith("К") or word.startswith("У") or word.startswith("Ц") or word.startswith("Й"):
#         return True
#     else:
#         return False

# com_acento = []

# for word in f:
#     if checa_maiusc(word) == True:
#         pass
#     else:
#         com_acento.append(word)


# g.writelines(com_acento)

# f.close()
# g.close()










################### TESTES #############################

# f = open("ukrainian stress.txt", "r", encoding="utf8")
# g = open("ukrainian stress filtrado.txt", "r", encoding="utf8")

# def checa_maiusc():
#     return True

# com_acento = []

#CHECA MAIUSCULA
# for word in f:
#     if word.startswith("А́"):
#         com_acento.append(word)

# print(com_acento)
# print(len(com_acento))


#PALAVRAS COM UMA E DUAS LETRAS
# for word in f:
#     if len(word) == 3 or len(word) == 4:
#         com_acento.append(word)

# print(com_acento)
# print(len(com_acento))

# g.writelines(com_acento)

# f.close()
# g.close()







############## REMOVENDO PALAVRAS COM 1 E 2 LETRAS ######################

# f = open("ukrainian stress filtrado base.txt", "r", encoding="utf8")
# # g = open("ukrainian stress filtrado.txt", "w", encoding="utf8")

# # REMOVER PALAVRAS COM 1 E 2 LETRAS
# # com_acento = ['є́ї\n', 'є́ю\n', 'її́\n']
# com_acento = []


# # g.writelines(com_acento)

# f.close()
# # g.close()






############## REMOVENDO ACENTOS ######################

# f = open("ukrainian stress filtrado.txt", "r", encoding="utf8")
# g = open("ukrainian stress filtrado plain.txt", "w", encoding="utf8")

# a = []

# for word in f:
#     a.append(word.lower().replace("є́", "є").replace("а́", "а").replace("ї́", "ї").replace("у́", "у").replace("и́", "и").replace("і́", "і").replace("о́", "о").replace("е́", "е").replace("я́", "я").replace("ю́", "ю"))


# g.writelines(a)

# f.close()
# g.close()


















############## REMOVENDO MAIUSCULAS ######################
# f = open("500k from wikipedia.txt", "r", encoding="utf8")
# g = open("500k from wikipedia filtrado em linha.txt", "w", encoding="utf8")

# def checa_maiusc(word):
#     if word.startswith("А́") or word.startswith("Е́") or word.startswith("І́") or word.startswith("У́") or word.startswith("О́") or word.startswith("Є́") or word.startswith("Я́") or word.startswith("Ї́") or word.startswith("Е́") or word.startswith("Ґ") or word.startswith("Ю") or word.startswith("Б") or word.startswith("Т") or word.startswith("И") or word.startswith("М") or word.startswith("С") or word.startswith("Ч") or word.startswith("Я") or word.startswith("Є") or word.startswith("Ж") or word.startswith("Д") or word.startswith("Л") or word.startswith("О") or word.startswith("Р") or word.startswith("П") or word.startswith("А") or word.startswith("В") or word.startswith("І") or word.startswith("Ф") or word.startswith("Ї") or word.startswith("Х") or word.startswith("З") or word.startswith("Щ") or word.startswith("Ш") or word.startswith("Г") or word.startswith("Н") or word.startswith("Е") or word.startswith("К") or word.startswith("У") or word.startswith("Ц") or word.startswith("Й"):
#         return True
#     else:
#         return False

# a = []

# # for word in f:
# #     if len(word) == 1 or len(word) == 2:
# #         pass
# #     else:
# #         a.append(word)


# for word in f:
#     a.append(word)

# b = " ".join(a)
# c = b.split()
# d = list(dict.fromkeys(c))

# e = []
# # for word in d:
# #     if len(word) == 1 or len(word) == 2:
# #         e.append(word)
# #     else:
# #         pass

# for word in d:
#     if checa_maiusc(word)  == True:
#         pass
#     else:
#         e.append(word)

# z= []
# for word in e:
#     if len(word) == 1 or len(word) == 2 or len(word) == 3:
#         pass
#     else:
#         z.append(word + " ")


# # print(e)
# # print(len(e))
# print(len(z))

# g.writelines(z)

# f.close()
# g.close()

# print("concluido")





############## TESTE ######################
# f = open("500k from wikipedia filtrado.txt", "r", encoding="utf8")
# f = open("ukrainian stress filtrado plain.txt", "r", encoding="utf8")
# # g = open("ukrainian stress filtrado plain em linha.txt", "w", encoding="utf8")

# a = []

# for word in f:
#     if word.startswith("й"):
#         a.append(word[:-1] +  " ")
#     # a.append(word[:-1] +  " ")

# # print(a)
# print(len(a))
# # g.writelines(a)

# f.close()
# # g.close()













############## COMPARA LISTAS ######################
### primeiro com a letra i curta

# f_com = open("ukrainian stress filtrado plain.txt", "r", encoding="utf8")
# f_sem = open("500k from wikipedia filtrado.txt", "r", encoding="utf8")
# f_acentuado = open("ukrainian stress filtrado base.txt", "r", encoding="utf8")
# # g = open("ukrainian stress filtrado plain em linha.txt", "w", encoding="utf8")

# letter = input("type letter ")
# a = []
# b = []
# c = []
# final = []

# for word in f_com:
#     if word.startswith(letter):
#         a.append(word[:-1] +  " ")
#     # a.append(word[:-1] +  " ")


# for word in f_sem:
#     if word.startswith(letter):
#         b.append(word[:-1] +  " ")

# for word in f_acentuado:
#     if word.startswith(letter):
#         c.append(word[:-1] +  " ")


# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == b[j]:
#             final.append(c[i])

# print(len(a))
# print(len(b))
# print(len(c))
# print(len(final))
# # print(final)

# f_com.close()
# f_sem.close()
# f_acentuado.close()
# g.close()

## faz letra por letra. Mas talvez vai ter q fazer naquele esquema de pop e append, pros casos em que a lista acentuada nao tem a palavra da lista 500k







############## REMOVER NUMEROS ######################
# f_com = open("500k from wikipedia filtrado.txt", "r", encoding="utf8")
# # temp = open("temp.txt", "w", encoding="utf8")

# def replace_i(word):
#     if word.find("i") == True:
#         new_word = word.replace("i", "і")
#         mylist.append(new_word.replace("\n",  " "))
#     else:
#         mylist.append(word.replace("\n",  " "))


# def checa_alfa(word):
#     if word.find("a") == True or word.find("e") == True or word.find("o") == True or word.find("u") == True or word.find(".") == True or word.find("q") == True or word.find("w") == True or word.find("r") == True or word.find("t") == True or word.find("y") == True or word.find("p") == True or word.find("s") == True or word.find("d") == True or word.find("f") == True or word.find("g") == True or word.find("h") == True or word.find("j") == True or word.find("k") == True or word.find("l") == True or word.find("z") == True or word.find("x") == True or word.find("c") == True or word.find("v") == True or word.find("b") == True or word.find("n") == True or word.find("m") == True :
#         pass
#     else:
#         # mylist.append(word)
#         replace_i(word)

# def checa_num(word):
#     if word.find("1") == True or word.find("2") == True or word.find("3") == True or word.find("4") == True or word.find("5") == True or word.find("6") == True or word.find("7") == True or word.find("8") == True or word.find("9") == True or word.find("0") == True or word.find("-") == True:
#         pass
#     else:
#         checa_alfa(word)

# # words =[]
# mylist =  []

# for word in f_com:
#     # if word.find("\u0032") == True:
#     if ascii(word).find("2") == True:
#         mylist.append(word)
#     # checa_num(word)


# print(len(mylist))
# # print(mylist)
# # print(type(mylist[0]))
# # print(ascii("своїх "))
# print(ascii("20-го\n"))
# print(ascii("світу-2022"))
# txt = "999світу-2022"
# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="utf8"))
# # print(ascii(sem_acento[4][:-1]))

# # temp.writelines(mylist)



# f_com.close()
# # temp.close()























############## BUSCAR PALAVRAS REPETIDAS ######################
# f = open("ukrainian stress filtrado plain em linha.txt", "r", encoding="utf8")
# rep = open("repetidas temp.txt", "w", encoding="utf8")

# list1 = []

# for word in f:
#     list1.append(word)

# list2 = " ".join(list1)
# list_final = list2.split(" ")

# repetidas = []

# for i in range(len(list_final)-2):
#     if list_final[i] == list_final[i+1]:
#         repetidas.append(list_final[i] + " ")

# print(len(repetidas))        

# rep.writelines(repetidas)

# # b = " ".join(a)
# # c = b.split()
# # d = list(dict.fromkeys(c))


# f.close()
# rep.close()


























































############## COMPARAR REPETIDAS COM A LISTA 500 ######################
# f = open("500k from wikipedia filtrado em linha.txt", "r", encoding="utf8")
# g = open("repetidas temp.txt", "r", encoding="utf8")
# rep = open("repetidas temp 500.txt", "w", encoding="utf8")

# list1 = []


# for word in f:
#     list1.append(word)


    

# list2 = " ".join(list1)
# list_final = list2.split(" ") #lista 500

# ######## repetidas

# reps = []
# for word in g:
#     reps.append(word)


# reps2 = " ".join(reps)
# repetidas = reps2.split(" ") #lista reps
# # repetidas = list(dict.fromkeys(reps3))



# repetidas_final = []

# for i in range(len(list_final)):
#     for j in range(len(repetidas)):
#         if list_final[i] == repetidas[j]:
#             repetidas_final.append(list_final[i] + " ")

# print(len(repetidas_final))        
# print(len(repetidas))        
# # print(len(list1))        
# # print(len(list2))        
# # print(len(list_final))        
# # print(len(list_final))        
# # print(len(reps3))
# # print(type (reps3))

# rep.writelines(repetidas_final)

# # b = " ".join(a)
# # c = b.split()
# # d = list(dict.fromkeys(c))


# f.close()
# g.close()
# rep.close()




















# agora tem q pegar o indice comparando a lista de repetidas 500 com a lista filtrado base
############## PEGAR INDICE DAS PALAVRAS REPETIDAS ######################
# f = open("repetidas temp 500.txt", "r", encoding="utf8")
# g = open("ukrainian stress filtrado plain em linha.txt", "r", encoding="utf8")
# indices = open("temp indices only.txt", "a", encoding="utf8")

# letter = "б"

# list1 = []

# for word in f:
#     list1.append(word)

# list2 = " ".join(list1)
# list_semi = list2.split(" ") #lista repetidas
# list_final = []
# for word in list_semi:
#     if word.startswith(letter):
#         list_final.append(word + ' ')


# original = []
# for word in g:
#     original.append(word)    

# og2 = " ".join(original)
# list_semi_og = og2.split(" ") #lista reps
# list_og = []
# for word in list_semi_og:
#     if word.startswith(letter):
#         list_og.append(word + ' ')


# index = []

# for i in range(len(list_final)):
#     for j in range(len(list_og)):
#         if list_final[i] == list_og[j]:
#             index.append(str(j) + " ")



# print(len(index))
# # print(index)

# indices.writelines(index)

# f.close()
# g.close()
# indices.close()















############## PEGAR INDICE DO ARQUIVO ORIGINAL ######################

# f = open("temp indices only.txt", "r", encoding="utf8")
# g = open("ukrainian stress filtrado plain em linha.txt", "r", encoding="utf8")
# h = open("ukrainian stress filtrado.txt", "r", encoding="utf8")
# indices = open("temp indices words only.txt", "a", encoding="utf8")


# teste1 = f.read()
# list_index = [ int(x) for x in teste1.split() ]

# #G
# original = []
# for word in g:
#     original.append(word)    

# og2 = " ".join(original)
# list_semi_og = og2.split(" ") #lista acentuada
# list_og = []

# #H
# acentuada = []
# for word in h:
#     acentuada.append(word[:-1])


# index = []


# # for i in list_index:
# #     index.append(list_semi_og[i] + "|" + list_semi_og[i])
# for i in range(len(list_index)):
#     if i%2 == 0:
#         index.append(acentuada[list_index[i]+3] + "|" + acentuada[list_index[i]+4] + " ")

# # print(len(index))
# # print(index[0:3])

# print(list_semi_og[1111111])
# print(acentuada[1111111])

# # indices.writelines(index)

# f.close()
# g.close()
# h.close()
# indices.close()

# # ESTÁ COM PROBLEMA -- ta dando erro no indice, ta pegando o indice errado




































############## PEGAR INDICE DO ARQUIVO ORIGINAL ######################
# f = open("500k from wikipedia filtrado em linha.txt", "r", encoding="utf8")
# g = open("ukrainian stress filtrado plain em linha.txt", "r", encoding="utf8")
# h = open("ukrainian stress filtrado.txt", "r", encoding="utf8")
# found_word = open("found.txt", "a", encoding="utf8")
# not_found_word = open("not found.txt", "a", encoding="utf8")

# letter = "а"

# teste1 = f.read()
# teste2 = [ x for x in teste1.split() ]
# list_500 = []
# for word in teste2:
#     if word.startswith(letter):
#         list_500.append(word + ' ')


# #G
# original = []
# for word in g:
#     original.append(word)    

# og2 = " ".join(original)
# list_semi_og = og2.split(" ") #lista acentuada
# list_plain = []
# for word in list_semi_og:
#     if word.startswith(letter):
#         list_plain.append(word + ' ')

# #H
# acentuada = []
# for word in h:
#     acentuada.append(word[:-1])

# list_acentuada = []
# for word in acentuada:
#     if word.startswith(letter):
#         list_acentuada.append(word + ' ')

# final_500 = []
# not_found = []

# # for i in range(len(list_500)):
# #     for j in range(len(list_plain)):
# #         if list_500[i] == list_plain[j]:
# #             final_500.append(list_acentuada[j])
# #         else:
# #             not_found.append(list_500[i])

# for word in list_500:
#     try:
#         n = list_plain.index(word)
#         final_500.append(list_acentuada[n])
#     except:
#         not_found.append(word)


# print(len(final_500))
# print(len(not_found))
# # print(len(list_500))
# # print(len(list_plain))
# # print(len(list_acentuada))


# # not_found_word.writelines(not_found)
# # found_word.writelines(final_500)

# f.close()
# g.close()
# h.close()
# not_found_word.close()
# found_word.close()







































############## BUSCAR PALAVRAS REPETIDAS ######################
# f = open("500k from wikipedia filtrado em linha.txt", "r", encoding="utf8")
# g = open("ukrainian stress filtrado plain em linha.txt", "r", encoding="utf8")
# h = open("ukrainian stress filtrado.txt", "r", encoding="utf8")
# dup_acentuado = open("reps acentuada.txt", "a", encoding="utf8")
# dup_plain = open("reps plain.txt", "a", encoding="utf8")

# letter = "я"
# # 
# #########
# #f -- lista 500
# f1 = f.read()
# f2 = [ x for x in f1.split() ]
# list_500 = []
# for word in f2:
#     if word.startswith(letter):
#         list_500.append(word + ' ')


# #g -- lista plain
# g1 = g.read()
# g2 = [ x for x in g1.split() ]
# list_plain = []
# for word in g2:
#     if word.startswith(letter):
#         list_plain.append(word + ' ')

# #h -- lista acentuada
# acentuada = []
# for word in h:
#     acentuada.append(word[:-1])
# list_acentuada = []
# for word in acentuada:
#     if word.startswith(letter):
#         list_acentuada.append(word + '')


# reps_acentuada = []
# reps_plain = []

# ###########
# for i in range(len(list_plain)-2):
#     if list_plain[i] == list_plain[i+1]:
#         reps_acentuada.append(list_acentuada[i] + "|" + list_acentuada[i+1] + " ")
#         reps_plain.append(list_plain[i] + " ")



# dup_acentuado.writelines(reps_acentuada)
# dup_plain.writelines(reps_plain)

# print(reps_acentuada[0])
# print(reps_plain[0])



# f.close()
# g.close()
# h.close()
# dup_acentuado.close()
# dup_acentuado.close()


#ai depois, tem q fazer uma nova lista das palavras da lista 500 que tem nessa lista de duplicados
























############## LISTA 500 NA LISTA REPS ######################
# f = open("500k from wikipedia filtrado em linha.txt", "r", encoding="utf8")
# g = open("reps acentuada.txt", "r", encoding="utf8")
# h = open("reps plain.txt", "r", encoding="utf8")
# dup_acentuado = open("acentuada final.txt", "w", encoding="utf8")
# dup_plain = open("plain final.txt", "w", encoding="utf8")

# # letter = "а"
# letter_arr = ['а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я']
# f1 = f.read()
# f2 = [ x for x in f1.split() ]
# g1 = g.read()
# g2 = [ x for x in g1.split() ]
# h1 = h.read()
# h2 = [ x for x in h1.split() ]
# # абвгдеєжзіїйклмнопрстуфхцчшщюя
# #########
# for letter in letter_arr:
#     print(letter)
#     #f -- lista 500
    
#     list_500 = []
#     for word in f2:
#         if word.startswith(letter):
#             list_500.append(word + ' ')
#     #g -- lista acentuada
    
#     list_acentuada = []
#     for word in g2:
#         if word.startswith(letter):
#             list_acentuada.append(word + ' ')
#     #h -- lista plain
    
#     list_plain = []
#     for word in h2:
#         if word.startswith(letter):
#             list_plain.append(word + ' ')
#     reps_acentuada = []
#     reps_plain = []
#     ###########
#     for i in range(len(list_500)):
#         for j in range(len(list_plain)):
#             if list_500[i] == list_plain[j]:
#                 reps_acentuada.append(list_acentuada[j] + "")
#                 reps_plain.append(list_plain[j] + "")
#     # ###########
#     # for i in range(len(list_plain)-2):
#     #     if list_plain[i] == list_plain[i+1]:
#     #         reps_acentuada.append(list_acentuada[i] + "|" + list_acentuada[i+1] + " ")
#     #         reps_plain.append(list_plain[i] + " ")       
#     dup_acentuado.writelines(reps_acentuada)
#     dup_plain.writelines(reps_plain)
#     # print(reps_acentuada[0])
#     # print(reps_plain[0])



# f.close()
# g.close()
# h.close()
# dup_acentuado.close()
# dup_acentuado.close()




















############## LISTA FINAL ######################
# f = open("500k from wikipedia filtrado em linha.txt", "r", encoding="utf8")
# g = open("ukrainian stress filtrado plain em linha.txt", "r", encoding="utf8")
# h = open("reps plain.txt", "r", encoding="utf8")
# base = open("ukrainian stress filtrado.txt", "r", encoding="utf8")
# dup_acentuado = open("acentuada final.txt", "a", encoding="utf8")
# dup_plain = open("plain final.txt", "a", encoding="utf8")
# not_found = open("not found.txt", "a", encoding="utf8")


# # letter = "а" , 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я'
# letter_arr = ["ґ", "и"]
# f1 = f.read()
# f2 = [ x for x in f1.split() ]
# g1 = g.read()
# g2 = [ x for x in g1.split() ]
# h1 = h.read()
# h2 = [ x for x in h1.split() ]
# base1 = []
# for word in base:
#     base1.append(word[:-1])
# # абвгдеєжзіїйклмнопрстуфхцчшщюя
# #########
# for letter in letter_arr:
#     print(letter)
#     #f -- lista 500
    
#     list_500 = []
#     for word in f2:
#         if word.startswith(letter):
#             list_500.append(word + ' ')
#     #g -- lista acentuada
    
#     list_plain = []
#     for word in g2:
#         if word.startswith(letter):
#             list_plain.append(word + ' ')
#     #h -- lista plain
    
#     list_reps = []
#     for word in h2:
#         if word.startswith(letter):
#             list_reps.append(word + ' ')

#     #base 
#     list_acentuada = []
#     for word in base1:
#         if word.startswith(letter):
#             list_acentuada.append(word + ' ')
#     final_acentuada = []
#     final_plain = []
#     list_not_found = []
#     ###########
#     not_in_reps = []
#     for word in list_500:
#         try:
#             list_reps.index(word)
#             continue
#         except:
#             not_in_reps.append(word)

#     for word in not_in_reps:
#         try:
#             n = list_plain.index(word)
#             final_acentuada.append(list_acentuada[n])
#             final_plain.append(list_plain[n])
#         except:
#             list_not_found.append(word)

#     dup_acentuado.writelines(final_acentuada)
#     dup_plain.writelines(final_plain)
#     not_found.writelines(list_not_found)
#     # print(reps_acentuada[0])
#     # print(reps_plain[0])


# f.close()
# g.close()
# h.close()
# base.close()
# dup_acentuado.close()
# dup_acentuado.close()



# ############TESTE FINAL
# f = open("acentuada final.txt", "r", encoding="utf8")
# g = open("plain final.txt", "r", encoding="utf8")
# # h = open("reps plain.txt", "r", encoding="utf8")
# # base = open("ukrainian stress filtrado.txt", "r", encoding="utf8")

# f1 = f.read()
# f2 = [ x for x in f1.split() ]
# g1 = g.read()
# g2 = [ x for x in g1.split() ]




# palavra1 = input("digite a palavra: ")
# palavra1.encode(encoding="ascii",errors="ignore")


# lista_com = []

# phrase = ""
# def find_word(palavra):
#     lista_sem = palavra.split()
#     lista_com = palavra.split()
    
#     for j in range(len(lista_sem)):
#         # print(lista_com)
#         for i in range(len(g2)):
#             if lista_sem[j] == g2[i]:
#                 #ADICIONAR A UMA NOVA LISTA
#                 lista_com.pop(j)
#                 lista_com.insert(j , f2[i])
#                 # print("aqui")
#                 # print(lista_com)
#     # print(" ".join(lista_com)) 
#     global phrase
#     phrase += " ".join(lista_com)
              
# # та хочеш йти зі мною після цього я тобі скажу

# find_word(palavra1)

# print("phrase")
# print(phrase)
# print(lista_com)

# f.close()
# g.close()












f = open("not found.txt", "a", encoding="utf8")

start = "відо́мо, Білору́сія, Білору́сії, Білору́сію, Білору́сією, Білору́сіє, вночі́ , хоча́, по́вністю, ни́ні, По́льща, По́льщі, По́льщу, По́льщею, По́льще, зо́всім "
words = start.replace(",", '').split()


final = []
for word in words:
   final.append('"' + word.lower().replace("є́", "є").replace("а́", "а").replace("ї́", "ї").replace("у́", "у").replace("и́", "и").replace("і́", "і").replace("о́", "о").replace("е́", "е").replace("я́", "я").replace("ю́", "ю") + '"' + ":" + '"' + word + '"' + ",")



f.writelines(final)

f.close()

print("OK")