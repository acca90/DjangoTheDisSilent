<?php

    function explodeXML($xml) {

        $objXML = new SimpleXmlElement($xml);

        if (strpos($xml, 'soap:') !== false) {
            $objXML->registerXPathNamespace('soap','http://www.portalfiscal.inf.br/nfe/wsdl/NfeConsulta2');
            $xml2 = (array)$objXML->xpath('//soap:Body');
        } else {
            $objXML->registerXPathNamespace('soapenv','http://www.w3.org/2003/05/soap-envelope');
            $xml2 = $objXML->xpath('//soapenv:Body');
        }

        $xml2[0]->children()->children()->children()->cStat;
        $xml2[0]->children()->children()->children()->xMotivo;
        $xml2[0]->children()->children()->children()->protNFe->infProt->dhRecbto;
        $xml2[0]->children()->children()->children()->protNFe->infProt->nProt;

    }

    explodeXML(file_get_contents("resp.xml"));
    explodeXML(file_get_contents("resp2.xml"));

    function dataForDb($data,$t=false) {
        $div = $t ? "T" : " ";
        $step1 = explode(" ",$data);
        $step2 = explode("/",$step1[0]);
        $step3 = implode("-",array_reverse($step2));
        return $step3.$div.$step1[1];
    }

    echo dataForDb("17/01/2016 14:30:00");


?>