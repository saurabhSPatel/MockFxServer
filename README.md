# MockFxServer
ReqFx will be validated with this scheama 
       <bridge:ReqFx xmlns:bridge="http://npci.org/bridge/schema/">
    <Head ver="2.0" ts="" orgId="" msgId="" prodType= "BRIDGE"/>
    <Txn id="" type="ReqFx" dealtSide="BUY" note="" refId="" refUrl=""/>
    <Fx remBankId="" beneBankId="" tenor="TODAY|TOM|SPOT|1D|1W|1M|2M|3M|4M|5M|6M|9M|1Y" validity="">
        <Amount fxProvId="" fsbId="" fCyAmount="" baseCurr="" targetCurr=""/>
    </Fx>
</bridge:ReqFx>
After Validation will be returning Random fx Rate.
