pip3 install virtualenv

virtualenv `pwd`/web-scraper
cd web-scraper
git clone --single-branch --branch develop https://github.com/PrajwalShenoy/StaticWebScraper.git
mv `pwd`/StaticWebScraper/files/geckodriver `pwd`/bin
cd ..
`pwd`/web-scraper/bin/pip3 install git+https://github.com/PrajwalShenoy/StaticWebScraper.git@develop
