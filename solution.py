def resolve( string):

    strg = 0

    for i in string.keys():

        if string[string[i]] < string[i]:

            string[i] = string[string[i]]

            strg+=1

    if (strg == 0):

        return

    else:

        resolve(string)

print("Sample Input")

s1 = input( )

s2 = input( )

s3 = input( )

string = {}

for i in range(97,123):

    string[chr(i)] = chr(i)

for i in range(len(s1)):

    if(s1[i] < s2[i]):

        string[s2[i]] = s1[i]

    elif(s1[i] > s2[i]):

        string[s1[i]] = s2[i]

    resolve(string)

result = ""

for i in range(len(s3)):

    result += string[s3[i]]

print("Output")

print(result)