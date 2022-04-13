# Задание 2
## Благодарность за CISCO ентому товарищу --> https://vk.com/zvuki_seksa

Для начала строим данную сетку по такому шаблону
![image](https://user-images.githubusercontent.com/81534024/163091653-a1b6994f-1e84-4a94-894a-2b76a3529cc1.png)
В конфигах серверов и компов меняем названия на нужные по заданию 
![image](https://user-images.githubusercontent.com/81534024/163091694-233879b6-82fa-4bdb-83f2-dfdd63fb074d.png)
Задача решается на примере билета 1 но применима ко всем остальным
Настраиваем рутер(маршрутизатор в графе CLI)
Router>enable 
Router#config terminal 
Router(config)#int fa0/0 
Router(config-if)#ip add 10.10.1.1 255.255.255.224 
Router(config-if)#no shutdown 
Router(config-if)#exit
Ip адрес рутера на 1 больше адреса сети, то есть если сеть 10.10.1.0/27 то ip рутера будет 10.10.1.1 а его маской по таблице масок (маска с префиксом \27) будет 255.255.255.224 (31 клиент в сети максимально) 
![image](https://user-images.githubusercontent.com/81534024/163091752-40e733b6-9813-49ce-a033-9f6b85a19187.png)
![image](https://user-images.githubusercontent.com/81534024/163091834-77862eda-e398-4588-88a1-7ec3f8d5ab16.png)
После этого на рутере надо настроить DHCP пул, то есть область ip адресов которые будут автоматически выдаваться клиентам сети
Router(config)#ip dhcp pool MY_LAN (название любое)
Router(dhcp-config)#network 10.10.1.0 255.255.255.224 (наша сеть с маской) 
Router(dhcp-config)#default-router 10.10.1.1 (адрес рутера)
Router(dhcp-config)#dns- сервер 10.10.1.10 (адрес DHCP сервака)
Убираем адреса с 10.10.1.1 по 10.10.1.10 из списка выдаваемых адресов
Router(dhcp-config)#exit
Router(config)#ip dhcp excluded-address 10.10.1.1 10.10.1.10 
Выбираем пк и на каждом настраиваем DHCP вместо static, пк должен подхватить адрес dns сервера и шлюза (рутера (маршрутизатора))
![image](https://user-images.githubusercontent.com/81534024/163091855-79e9375c-5e5e-4303-992c-fffa2be639df.png)
Збс
Идем дальше
Настраиваем DNS сервер, переходим во вкладку Desktop -> ip configuration и выставляем sttic параметры dns сервера
![image](https://user-images.githubusercontent.com/81534024/163091869-fcdefb3c-27f9-4fab-8160-135d54e26292.png)
Во вкладке Services открываем панель DNS и добавляем названия компов и их ip адреса которые можно получить командой ipconfig в консоли пк
![image](https://user-images.githubusercontent.com/81534024/163091882-a19e976f-e2ee-45be-87a4-5d53a29912f0.png)
Настраиваем DHCP сервер
Во вкладке Desktop ip conf ставим параметр dhcp
![image](https://user-images.githubusercontent.com/81534024/163091891-e8de7f7a-4dda-4f67-b7aa-91b2256f1510.png)
После во вкладке services DHCP прописываем параметры нашей сети
![image](https://user-images.githubusercontent.com/81534024/163091907-095fca20-3966-4657-b2ae-55301cd28422.png)
Жмем add
p,c
збс
Проверка работы DNS - сервера, в командной строке пк прописываем ping pc-kkmt-2, если пинг проходит - збс
![image](https://user-images.githubusercontent.com/81534024/163091923-a125b1c5-0636-4c6c-a032-f35c4a75890b.png)
Настройка WEB сервера проста, во вкладке Desktop ip config ставим dhcp
![image](https://user-images.githubusercontent.com/81534024/163091942-5d6aa0ab-8aa1-42df-b71f-d7e9dabcc42d.png)
Во вкладке services HTTP включаете http но не включаете https (защищенный протокол)
![image](https://user-images.githubusercontent.com/81534024/163091961-2ae5b2fc-05ab-44f9-adc1-b7852a6f6d28.png)
Проверка Web сервера, заходите в PC во вкладку Desktop - > Web browser и вбиваете адрес ip веб сервера и voila работает
![image](https://user-images.githubusercontent.com/81534024/163091973-d8216a23-707c-4aa5-b908-6d4d3d0d7b6b.png)
