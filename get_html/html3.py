import urllib.request

response = urllib.request.urlopen(
    'http://www.eigonary.com/p/37?nCP=5')
content = response.readline()
content = content.decode('utf-8')

print(content)

with open('test4.txt', 'w') as f:

    while content:

        if '<a href=' in content:
            a = []
            content = response.readline()
            content = content.decode('utf-8')
            content = content.replace('\t','')
            content = content.replace('\r\n', '')
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
            print(a)
        content = response.readline()
        content = content.decode('utf-8')


