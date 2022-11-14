import unittest
import HtmlTestRunner

from Intalnirea10.test_alerts import Alerts
from Intalnirea10.test_keys import Keyboard
from Intalnirea10.test_context_menu import ContextMenu
from Intalnirea10.test_auth import Authentication
from Intalnirea10.test_browser import Browser


class TestSuite(unittest.TestCase):
    # pentru ca am importat toata libraria este nevoie sa specificam in fata clasei TestCase

    # libraria din care sa fie extrasa
    # Daca importam doar libraria, sistemul va avea doar adresa de identificare a librariei,
    # nu si a clasei TestCase
    # Suita de teste = un set de teste care pot fi rulate in acelasi timp
    def test_suite(self):  # numele metodei este predefinit si NU trebuie schimbat
        teste_de_rulat = unittest.TestSuite() # am creat un obiect al clasei TestSuite
        # prin obiectul teste_de_rulat vom accesa metoda addTests
        # metoda addTests primeste ca si parametru o lista de teste care se doreste a fi executate
        # lista de teste va fi separata prin virgula

        # teste_de_rulat.addTests([]) metoda add tests, apelata fara parametru

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(Browser)
        ])

        runner = HtmlTestRunner.HTMLTestRunner\
                (
            combine_reports=True,
            report_title='TestReport',
            report_name='Nume Rezultat Teste 10.11.2022'
            )

        runner.run(teste_de_rulat)

