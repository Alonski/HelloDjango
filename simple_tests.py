from django.test import TestCase

class SimpleTestCase(TestCase):
    def test_multiply_ok(self):
        url = "/mult/4/5/"
        expected = "4 X 5 = 20"

        resp = self.client.get(url)

        self.assertEquals(resp.status_code, 200)
        self.assertContains(resp, expected)

    def test_404(self):
        url = "/564651/"
        expected = "404 Error"

        resp = self.client.get(url)

        self.assertEquals(resp.status_code, 404)
        self.assertContains(resp, expected, status_code=404)
