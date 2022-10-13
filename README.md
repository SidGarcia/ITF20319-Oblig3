# ITF20319-Oblig3
Software Engineering and Testing - Python og pytest

Har implementert modulen pytest-github-report (https://pypi.org/project/pytest-github-report/) og benyttet en kodeblokk fra GitHub-repoen (https://github.com/vsoch/pytest-github-report/blob/main/.github/workflows/main.yml) for å bygge GitHub Actions-workflow.

https://github.com/SidGarcia/ITF20319-Oblig3/actions/runs/3241499493/workflow

Denne workflowen kjøres når filer blir pushet til denne repoen:

* Setter opp Python
* Installerer/sjekker avhengigheter gitt i requirements.txt
* Rapporterer akseptansekriteriene på tre ulike formater via pytest --github-report tests
	
Årsvariablen 'year' er hardkodet som 2000 for testing av kriterier, og kan enkelt kobles til annen funksjon eller system.
