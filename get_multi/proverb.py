import urllib.request

url_name1 = 'http://www.eigonary.com/p/394?nCP='

with open('aa.txt', 'a') as f:
    for i in range(1):
        url_name2 = str(i+1)
        url_name = url_name1 + url_name2
        #print(url_name)
        response = urllib.request.urlopen(url_name)

        content = response.readline()
        content = content.decode('utf-8')

        #print(content)


        while content:
            content = response.readline()
            content = content.decode('utf-8')
            if '<a href=' in content:
                content = response.readline()
                content = content.decode('utf-8')
                break

        while content:

            if '<a href=' in content:
                a = []
                content = response.readline()
                content = content.decode('utf-8')
                content = content.replace('\t','')
                content = content.replace('\r\n', '')
                if content == '' or content[0] == ' ' or content[0] == '<':
                    break
                f.write(content)
                f.write('*')
                a.append(content)
                content = response.readline()
                content = response.readline()
                content = content.decode('utf-8')
                content = content.replace('\t', '')
                content = content.replace('\r', '')
                f.write(content)
                a.append(content)
                #print(a)
            content = response.readline()
            content = content.decode('utf-8')
