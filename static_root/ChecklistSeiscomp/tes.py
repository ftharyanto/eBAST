import requests

url = 'https://script.google.com/macros/s/AKfycbxPVOb8TVUbu8q8c23d4jEJdTDEJZLp9me8Z7rkv0pbQ0m7jcNhcC6jwgt2bNfEe_vTmA/exec'


metadata = {
    'kelompok': '2',
    'operator1': 'fajar',
    'operator2': 'tri',
    'tanggal': '2023-05-10',
    'data1': {
                'gaps': ['ACBM', 'ALTI', 'AAFM'],
                'spikes': ['ACBM', 'ALTI', 'AAFM'],
                'blanks': ['ACBM', 'ALTI', 'AAFM'],
    },
    'data2': {
        'gaps': ['ACBM', 'ALTI', 'AAFM'],
        'spikes': ['ACBM', 'ALTI', 'AAFM'],
        'blanks': ['ACBM', 'ALTI', 'AAFM'],
    },
}


response = requests.post(url, json=metadata)
print(response.text)
