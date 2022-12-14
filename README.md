# enviro-project
Fulfil-TEAM project

Menga bu loyihani foydali tarafi shunda bo'ldiki, bu sayt 3 tilda ekanligi, chunki men realni, o'zim saytni 3 ta tilda ishlaydigan qila oldim. Yana bir foydali tarafi orqaga (back) tugmasi borligi, chunki bunday tartibda o'zim qilib ko'rmagandim. Unda product-da turib orqaga usha product-ni category_id-isi bo'yicha qaytish edi. Shu holatni ham o'zim qildim va ozroq bo'lsa ham o'zimda o'sish bo'layotganligidan xursandman.

Ishlatilgan texnologiyalar:

"modeltranslation", "i18n_patterns", "gettext_lazy"

{% get_current_language as LANGUAGE_CODE %}

{% get_available_languages as LANGUAGES %}

{% get_language_info_list for LANGUAGES as languages %}

{% for lang in languages %}

<a href="/{{ lang.code }}/">{{ lang.name_local }}</a>

{% endfor %}

{% trans 'Products' %} bunda Product matnini uchta tilga o'zgartirib beradi.

![image](https://user-images.githubusercontent.com/91982815/207510254-fa18a873-509b-4e39-803a-afa753d13e13.png)

![image](https://user-images.githubusercontent.com/91982815/207510462-a0e47168-0778-4eb4-bd3f-e2ab360405aa.png)



English language
![image](https://user-images.githubusercontent.com/91982815/204130996-f7de47ac-0ee6-4f4c-b91d-21dafacdea79.png)


Русский
![image](https://user-images.githubusercontent.com/91982815/204131034-2a0ce192-fcc7-465c-8870-db5bb4291264.png)


Uzbek tilida
![image](https://user-images.githubusercontent.com/91982815/204131067-d96a022c-72b9-44c4-8f86-abd00a5c326e.png)


