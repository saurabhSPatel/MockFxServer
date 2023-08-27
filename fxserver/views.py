from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from lxml import etree

@csrf_exempt
def processreqfx(request):
    try:
        # Get the raw XML data from the request
        xml_data = request.body.decode('utf-8')

        # Define the XML schema for validation
        schema = '''
       <bridge:ReqFx xmlns:bridge="http://npci.org/bridge/schema/">
    <Head ver="2.0" ts="" orgId="" msgId="" prodType= "BRIDGE"/>
    <Txn id="" type="ReqFx" dealtSide="BUY" note="" refId="" refUrl=""/>
    <Fx remBankId="" beneBankId="" tenor="TODAY|TOM|SPOT|1D|1W|1M|2M|3M|4M|5M|6M|9M|1Y" validity="">
        <Amount fxProvId="" fsbId="" fCyAmount="" baseCurr="" targetCurr=""/>
    </Fx>
</bridge:ReqFx>
        '''

        # Parse the XML and validate against the schema
        parser = etree.XMLParser(schema=etree.XMLSchema(etree.XML(schema)))
        root = etree.fromstring(xml_data, parser)

        # Process the validated XML request
        response_xml = """
            <!-- For Fx Provider -->
            <bridge:RespFx xmlns:bridge="http://npci.org/bridge/schema/">
                <Head ver="1.0|2.0" ts="" orgId="" msgId="" prodType="BRIDGE"/>
                <Txn id="" note="" refId="" refUrl="" type="Fx" />
                <Resp reqMsgId="" result="SUCCESS" errCode=""/>
                <Amount fsbId="" fxProvId="" baseCurr="" fCyAmount="" targetCurr="" fxRate="" uniQuotesId="" valEndTs="">
                    <!-- Timestamp will be GMT -->
                    <Fee name="FXPROV" value="" currency="LCy" valEndTs=""/>
                    <!-- currency = Currency code -->
                </Amount>
            </bridge:RespFx>
        """
        return HttpResponse(response_xml, content_type="text/xml")

    except etree.XMLSyntaxError:
        # Return 400 Bad Request if XML is not well-formed
        return HttpResponseBadRequest("Invalid XML Request")
