import requests

res =  requests.get('https://gorest.co.in/public/v2/users')

#print(res)

#print(rest.json()[])

for record in res.json():
    if record["status"] == "active":
        print(record)
    else: 
        print("skipped!")

#requirements provided: 
'''get all the users and 
get the emails with .io extension 
https://gorest.co.in/public/v2/users/100
'''


[
  {
    "id": 2428,
    "name": "Abhaidev Pillai",
    "email": "pillai_abhaidev@king-schaden.co",
    "gender": "male",
    "status": "inactive"
  },
  {
    "id": 2427,
    "name": "Gemine Mahajan I",
    "email": "mahajan_gemine_i@emard-stroman.org",
    "gender": "female",
    "status": "inactive"
  },
  {
    "id": 2426,
    "name": "Ms. Rajiv Gandhi",
    "email": "ms_gandhi_rajiv@legros-towne.org",
    "gender": "male",
    "status": "active"
  },
  {
    "id": 2425,
    "name": "Sarada Patil",
    "email": "patil_sarada@hoppe-hessel.net",
    "gender": "male",
    "status": "active"
  },
  {
    "id": 2424,
    "name": "Anuraag Embranthiri",
    "email": "anuraag_embranthiri@turner.com",
    "gender": "female",
    "status": "active"
  },
  {
    "id": 2423,
    "name": "Inder Bandopadhyay",
    "email": "inder_bandopadhyay@stamm.info",
    "gender": "male",
    "status": "active"
  },
  {
    "id": 2422,
    "name": "Chanakya Joshi",
    "email": "joshi_chanakya@ondricka.com",
    "gender": "female",
    "status": "active"
  },
  {
    "id": 2421,
    "name": "Ujjwal Pothuvaal DC",
    "email": "ujjwal_pothuvaal_dc@swaniawski.io",
    "gender": "male",
    "status": "inactive"
  },
  {
    "id": 2419,
    "name": "Agnimitra Ahuja",
    "email": "agnimitra_ahuja@cummings.biz",
    "gender": "male",
    "status": "inactive"
  },
  {
    "id": 2418,
    "name": "Bhagwanti Bandopadhyay DO",
    "email": "bandopadhyay_bhagwanti_do@gulgowski-lindgren.io",
    "gender": "female",
    "status": "active"
  },
  {
    "id": 2417,
    "name": "Priyala Khanna",
    "email": "khanna_priyala@spinka.com",
    "gender": "male",
    "status": "inactive"
  },
  {
    "id": 2416,
    "name": "Achintya Nambeesan",
    "email": "nambeesan_achintya@bartoletti.info",
    "gender": "male",
    "status": "inactive"
  },
  {
    "id": 2415,
    "name": "Bhargavi Bhat CPA",
    "email": "cpa_bhat_bhargavi@hessel-daugherty.io",
    "gender": "male",
    "status": "inactive"
  },
  {
    "id": 2413,
    "name": "Dr. Saraswati Gill",
    "email": "saraswati_dr_gill@roberts.io",
    "gender": "male",
    "status": "inactive"
  },
  {
    "id": 2412,
    "name": "Tapan Iyer",
    "email": "iyer_tapan@dubuque.org",
    "gender": "male",
    "status": "active"
  },
  {
    "id": 2411,
    "name": "Rukmin Joshi",
    "email": "rukmin_joshi@bode-kovacek.net",
    "gender": "male",
    "status": "active"
  },
  {
    "id": 2410,
    "name": "Rita Kocchar",
    "email": "kocchar_rita@runolfsdottir.net",
    "gender": "female",
    "status": "inactive"
  },
  {
    "id": 2409,
    "name": "Dhanalakshmi Chaturvedi",
    "email": "chaturvedi_dhanalakshmi@witting.com",
    "gender": "female",
    "status": "inactive"
  },
  {
    "id": 2408,
    "name": "Arya Asan JD",
    "email": "jd_arya_asan@blick.co",
    "gender": "male",
    "status": "active"
  },
  {
    "id": 2407,
    "name": "Anjushree Iyer",
    "email": "anjushree_iyer@corwin-mayer.net",
    "gender": "male",
    "status": "active"
  }
]