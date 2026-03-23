import pandas as pd


def load_data():

    train = pd.read_csv('./data/train.csv',nrows=100000)
    test = pd.read_csv('./data/test.csv',nrows=100000)

    #print(train.shape)
    #print(train.head(5))

    X = train.drop(columns=['ID','label'])
    y = train['label']
    X_test = test.drop(columns=['ID'])

    X['URL'] = X['URL'].str.replace('[.]','.',regex=False)
    X_test['URL'] = X_test['URL'].str.replace('[.]','.',regex=False)

    X = make_features(X)
    X_test = make_features(X_test)

    return X, y, X_test



def make_features(df):
    #1차 선정
    df = df.copy()
    hostname = df['URL'].str.split('/').str[0]

    df['url_length'] = df['URL'].str.len()
    df['hostname_length'] = hostname.str.len()

    df['dot_count'] = df['URL'].str.count(r'\.')
    df['dash_count'] = df['URL'].str.count(r'-')
    df['underscore_count'] = df['URL'].str.count(r'_')
    df['slash_count'] = df['URL'].str.count(r'/')
    df['digit_count'] = df['URL'].str.count(r'\d')
    df['backslash_count'] = df['URL'].str.count(r'\\')

    df['has_ip'] = df['URL'].str.contains(r'\d+\.\d+\.\d+\.\d+',regex=True).astype(int)
    df['has_http'] = df['URL'].str.contains('http',case=False,regex=False).astype(int) 
    
    #2차 선정
    df['has_login'] = df['URL'].str.contains('login',case=False,regex=False).astype(int)
    df['has_verify'] = df['URL'].str.contains('verify',case=False,regex=False).astype(int)
    df['has_update'] = df['URL'].str.contains('update',case=False,regex=False).astype(int)
    df['has_secure'] = df['URL'].str.contains('secure',case=False,regex=False).astype(int)    
    df['has_account'] = df['URL'].str.contains('account',case=False,regex=False).astype(int)    
    df['has_bank'] = df['URL'].str.contains('bank',case=False,regex=False).astype(int)    
    df['has_money'] = df['URL'].str.contains('money',case=False,regex=False).astype(int)    
    df['has_benefit'] = df['URL'].str.contains('benefit',case=False,regex=False).astype(int)    
    df['has_congratulat'] = df['URL'].str.contains('congratulat',case=False,regex=False).astype(int)

    df['has_keyword_count'] = df[[
        'has_login','has_verify','has_update','has_secure',
        'has_account','has_bank','has_money','has_benefit','has_congratulat'
    ]].sum(axis = 1)
    
    df['subdomain_count'] = (hostname.str.count(r'\.')-1).clip(lower = 0)

    #3차 선정
    df['at_count'] = df['URL'].str.count(r'@')
    df['question_count'] = df['URL'].str.count(r'\?')
    df['equal_count'] = df['URL'].str.count(r'=')


    df = df.drop(columns = ['URL'])

    return df