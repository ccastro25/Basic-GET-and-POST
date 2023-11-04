const puppeteer = require('puppeteer');


module.exports = async function getresultFromDom() {
    const browser = await puppeteer.launch();


        page = await browser.newPage();
        await page.goto('file:///Users/caonabocastro/Desktop/basicRouting/BasicGetAndPost/index.html', {waitUntil: 'load'});


    const newPage = await page.evaluate(() => {

        return  document.getElementById("result").innerHTML;

        });

     console.log(newPage)

  };

