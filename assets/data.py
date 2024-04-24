scales_chords = {
    'major':{
        'C':['C major', 'D minor', 'E minor', 'F major', 'G major', 'A minor', 'B diminished'],
        'G':['G major', 'A minor', 'B minor', 'C major', 'D major', 'E minor', 'F sharp diminished'],
        'D':['D major', 'E minor', 'F sharp minor', 'G major', 'A major', 'B minor', 'C sharp diminished'],
        'A':['A major', 'B minor', 'C sharp minor', 'D major', 'E major', 'F sharp minor', 'G sharp diminished'],
        'E':['E major', 'F sharp minor', 'G sharp minor', 'A major', 'B major', 'C sharp minor', 'D sharp diminished'],
        'B':['B major', 'C sharp minor', 'D sharp minor', 'E major', 'F sharp major', 'G sharp minor', 'A sharp diminished'],
        'F sharp':['F sharp major', 'G sharp minor', 'B flat minor', 'B major', 'D flat major', 'D sharp minor', 'E sharp diminished'],
        'D flat':['D flat major', 'D sharp minor', 'F minor', 'F sharp major', 'A flat major', 'B flat minor', 'C diminished'],
        'A flat':['A flat major', 'B flat minor', 'C minor', 'D flat major', 'E flat major', 'F minor', 'G diminished'],
        'E flat':['E flat major', 'F minor', 'G minor', 'A flat major', 'B flat major', 'C minor', 'D diminished'],
        'B flat':['B flat major', 'C minor', 'D minor', 'E flat major', 'F major', 'G minor', 'A diminished'],
        'F':['F major', 'G minor', 'A minor', 'B flat major', 'C major', 'D minor', 'E diminished']
    },
    'minor':{
        'A':['A minor', 'B diminished', 'C major', 'D minor', 'E minor', 'F major', 'G major'],
        'E':['E minor', 'F sharp diminished', 'G major', 'A minor', 'B minor', 'C major', 'D major'],
        'B':['B minor', 'C sharp diminished', 'D major', 'E minor', 'F sharp minor', 'G major', 'A major'],
        'F sharp':['F sharp minor', 'G sharp diminished', 'A major', 'B minor', 'C sharp minor', 'D major', 'E major'],
        'C sharp':['C sharp minor', 'D sharp diminished', 'E major', 'F sharp minor', 'G sharp minor', 'A major', 'B major'],
        'G sharp':['G sharp minor', 'A sharp diminished', 'B major', 'C sharp minor', 'D sharp minor', 'E major', 'F sharp major'],
        'D sharp':['D sharp minor', 'E sharp diminished', 'F sharp major', 'G sharp minor', 'B flat minor', 'B major', 'D flat major'],
        'B flat':['B flat minor', 'C diminished', 'D flat major', 'D sharp minor', 'F minor', 'F sharp major', 'A flat major'],
        'F':['F minor', 'G diminished', 'A flat major', 'B flat minor', 'C minor', 'D flat major', 'E flat major'],
        'C':['C minor', 'D diminished', 'E flat major', 'F minor', 'G minor', 'A flat major', 'B flat major'],
        'G':['G minor', 'A diminished', 'B flat major', 'C minor', 'D minor', 'E flat major', 'F major'],
        'D':['D minor', 'E diminished', 'F major', 'G minor', 'A minor', 'B flat major', 'C major']
    }
}

options_mode = {'Major':'major', 'Minor':'minor'}
options_base_major = {'C':1, 'G':2, 'D':3, 'A':4, 'E':5, 'B':6, 'F sharp':7, 'D flat':8, 'A flat':9, 'E flat':10, 'B flat':11, 'F':12}
options_base_minor = {'A':1, 'E':2, 'B':3, 'F sharp':4, 'C sharp':5, 'G sharp':6, 'D sharp':7, 'B flat':8, 'F':9, 'C':10, 'G':11, 'D':12}

chords = {'E minor':{'str1':'0','str2':'0','str3':'0','str4':'2', 'str5':'2','str6':'0'}, 
          'E major':{'str1':'0','str2':'0','str3':'1','str4':'2', 'str5':'2','str6':'0'}, 
          'E sharp diminished':{'str1':'X','str2':'-','str3':'2','str4':'4', 'str5':'3','str6':'1', 'options':'Presented as F diminished'},
          'E diminished':{'str1':'0','str2':'X','str3':'0','str4':'2', 'str5':'1','str6':'0'}, 
          'E flat major':{'str1':'3','str2':'4','str3':'3','str4':'5', 'str5':'X','str6':'X'}, 
          'F major':{'str1':'1','str2':'1','str3':'2','str4':'3', 'str5':'3','str6':'1'},
          'F minor':{'str1':'1','str2':'1','str3':'1','str4':'3', 'str5':'3','str6':'1'}, 
          'F sharp diminished':{'str1':'5','str2':'7','str3':'5','str4':'4', 'str5':'X','str6':'X'},
          'F sharp minor':{'str1':'2','str2':'2','str3':'2','str4':'4', 'str5':'4','str6':'2'},
          'F sharp major':{'str1':'2','str2':'2','str3':'3','str4':'4', 'str5':'4','str6':'2'},
          'G major':{'str1':'3','str2':'3','str3':'0','str4':'0', 'str5':'2','str6':'3'}, 
          'G minor':{'str1':'3','str2':'3','str3':'3','str4':'5', 'str5':'5','str6':'3'},
          'G sharp diminished':{'str1':'4','str2':'0','str3':'4','str4':'0', 'str5':'2','str6':'4'}, 
          'G diminished':{'str1':'3','str2':'2','str3':'0','str4':'X', 'str5':'1','str6':'3'},
          'G sharp minor':{'str1':'4','str2':'4','str3':'4','str4':'6', 'str5':'6','str6':'4'},
          'A minor':{'str1':'0','str2':'1','str3':'2','str4':'2', 'str5':'0','str6':'X'},
          'A major':{'str1':'0','str2':'2','str3':'2','str4':'2', 'str5':'0','str6':'X'},
          'A diminished':{'str1':'X','str2':'1','str3':'X','str4':'1', 'str5':'0','str6':'X'},
          'A sharp diminished':{'str1':'0','str2':'2','str3':'X','str4':'2', 'str5':'1','str6':'X'},
          'A flat major':{'str1':'4','str2':'4','str3':'5','str4':'6', 'str5':'6','str6':'4'},
          'B minor':{'str1':'2','str2':'3','str3':'4','str4':'4', 'str5':'2','str6':'X'}, 
          'B major':{'str1':'2','str2':'4','str3':'4','str4':'4', 'str5':'2','str6':'X'},
          'B diminished':{'str1':'1','str2':'0','str3':'4','str4':'0', 'str5':'2','str6':'X'},
          'B flat minor':{'str1':'1','str2':'2','str3':'3','str4':'3', 'str5':'1','str6':'X'}, 
          'B flat major':{'str1':'1','str2':'3','str3':'3','str4':'3', 'str5':'1','str6':'X'}, 
          'C major':{'str1':'0','str2':'1','str3':'0','str4':'2', 'str5':'3','str6':'X'}, 
          'C minor':{'str1':'3','str2':'4','str3':'5','str4':'5', 'str5':'3','str6':'X'},
          'C sharp diminished':{'str1':'0','str2':'2','str3':'0','str4':'2', 'str5':'4','str6':'X'},
          'C sharp minor':{'str1':'4','str2':'5','str3':'6','str4':'6', 'str5':'4','str6':'X'}, 
          'C diminished':{'str1':'2','str2':'1','str3':'X','str4':'1', 'str5':'3','str6':'X'},  
          'D minor': {'str1':'1','str2':'3','str3':'2','str4':'0', 'str5':'X','str6':'X'}, 
          'D major':{'str1':'2','str2':'3','str3':'2','str4':'0', 'str5':'X','str6':'X'},
          'D diminished':{'str1':'1','str2':'3','str3':'1','str4':'0', 'str5':'X','str6':'X'}, 
          'D sharp minor':{'str1':'6','str2':'7','str3':'8','str4':'8', 'str5':'6','str6':'X'},
          'D sharp diminished':{'str1':'2','str2':'4','str3':'2','str4':'1', 'str5':'X','str6':'X'},
          'D flat major':{'str1':'4','str2':'6','str3':'6','str4':'6', 'str5':'4','str6':'X'}
          }