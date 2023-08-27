from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from fxserver.views import processreqfx

class ProcessReqFxViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_valid_xml_request(self):
        xml_data = '''
        <bridge:ReqFx xmlns:bridge="http://npci.org/bridge/schema/">
            <!-- Your valid XML request data here -->
        </bridge:ReqFx>
        '''
        request = self.factory.post(reverse('processreqfx'), data=xml_data, content_type='text/xml')
        response = processreqfx(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<bridge:RespFx', response.content)

    def test_invalid_xml_request(self):
        xml_data = '''
        <bridge:InvalidReqFx xmlns:bridge="http://npci.org/bridge/schema/">
            <!-- Your invalid XML request data here -->
        </bridge:InvalidReqFx>
        '''
        request = self.factory.post(reverse('processreqfx'), data=xml_data, content_type='text/xml')
        response = processreqfx(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Invalid XML Request')

    def test_missing_required_element(self):
        # Test a request missing a required element
        xml_data = '''
        <bridge:ReqFx xmlns:bridge="http://npci.org/bridge/schema/">
            <!-- Your XML request missing a required element -->
        </bridge:ReqFx>
        '''
        request = self.factory.post(reverse('processreqfx'), data=xml_data, content_type='text/xml')
        response = processreqfx(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Invalid XML Request')

    def test_empty_xml_request(self):
        # Test an empty XML request
        xml_data = ''
        request = self.factory.post(reverse('processreqfx'), data=xml_data, content_type='text/xml')
        response = processreqfx(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Invalid XML Request')
