const fetch = require("node-fetch");
const request = require("request");


var username = 'rifat'
var password = 'Rafi4141'
var options = {

  url: 'http://31.145.42.4/issmanager/giris',
  headers: { 'User-Agent': 'Mozilla/5.0' },
  auth: {
    user: username,
    password: password
  }
}

request(options, function (err, res, body) {
  if (err) {
    console.dir(err)
    return
  }
  console.dir('headers', res.headers)
  console.dir('status code', res.statusCode)
  console.dir(body)
})
