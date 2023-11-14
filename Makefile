setup: requirements.txt
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.txt -q --no-cache-dir

venv:
	. .venv/bin/activate

crawl:
	(cd scraper && scrapy crawl products -a parse_limit=$(parse_limit) && cd ..) || cd .. 