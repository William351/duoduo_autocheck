# auto_checkin.py
import requests

url = "https://api.duoduo.link/api"
headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Ddtk": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVuaWQiOiJvZ0Jwb3hORTBreTVEUU4xTXVPaGdycG53ZE54IiwiaWF0IjoxNzM1OTU3Njg1LCJleHAiOjE3NTE1MDk2ODV9.3YJdkSJWFuk-HiCYcmVFHCF40uIN7MW1YSg8pdjRHYE"
}
data = {
    "params": "uyn50u+n1wUDDZA0UEfe681RIK3Wnss6l9wiY4R61wNTII6K/mKoI6p/Idm93Pp8QIKOeFt57sSDxw==",
    "key": "DkwyBJfInVKK7L8ZNqN1GHkZUb9KpHCSbguHalx61tuOaTBc6Y9zX251nbdaG54Wdz1CGfm7TNmJkwF+gWWt4Ya5RB8YpdBdExZ28E43L53pgNOYnaygJyIicB8TdaHQZm3UDKCSx/EZnnHfxTI9ebDtCeAMBGjJ7G6tkDLHnqO1Ss/nKzCWDxLdO2izMxXiA5eXx0vdlq9qJSSn6Eqjc9pcgCCWDTvRovYJrCu3dHOWWwtZBP8bJ4Ncbj0013TJD2vsskvwxc/lqraCwoCn+KFtEwMcuBNIO3/LFIRkF6dbMwPqtwTmcdOh6yUztpaPFK5lQ/tlf82EAwduenbXJdGLHuSNf+hZpRIDru/YPzM2ETyy7qEkpVH23V4/+oyNovVjYk4axfiAgrF+qm9DxLJQGJ61ANk85Ox08JuRPVxIBkU+5w80D3JQX7Fs9F4QmGJc3WH13N5qsG+RLravvOr36jUucQro5OErJqTPJvdqMiDw5HxzJ/lFoa2J4htZNuybC6DI+BcNe2YRZ18wzGUgMhaFFWxHloYc36MldiphWQpq5AqV8l08eBheE0KNRzfWeKlw1m83jlFasCMM9hVkm+SOIVs2j9IDFtN/DmorwJ2on6BKapFFR1IH5PH0Ei8g7g3WD5IpDkWGNjDg83V4k0a7vkHKEJmBmZQOo/A="
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("签到成功:")
else:
    print("签到失败:", response.status_code, response.text)
