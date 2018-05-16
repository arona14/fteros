# -*- coding: utf-8 -*-

tokenXML = """<?xml version="1.0" encoding="UTF-8"?>
	<SOAP-ENV:Envelope 
	xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
	   <SOAP-ENV:Header>
	     <ns3:MessageHeader xmlns:ns2="http://www.w3.org/2000/09/xmldsig#"
	       xmlns:ns3="http://www.ebxml.org/namespaces/messageHeader"
	       xmlns:ns4="http://www.w3.org/1999/xlink" 
	xmlns:ns5="http://schemas.xmlsoap.org/ws/2002/12/secext">
	       <ns3:From>
	<ns3:PartyId>sample.url.of.sabre.client.com</ns3:PartyId>
	       </ns3:From>
	       <ns3:To>
	<ns3:PartyId>webservices.sabre.com</ns3:PartyId>
	       </ns3:To>
	       <ns3:CPAId>WR17</ns3:CPAId>
	<ns3:ConversationId>InitialConversationIdNo_1</ns3:ConversationId>
	       <ns3:Service>SessionCreateRQ</ns3:Service>
	       <ns3:Action>SessionCreateRQ</ns3:Action>
	     </ns3:MessageHeader>
	     <ns5:Security xmlns:ns2="http://www.w3.org/2000/09/xmldsig#"
	       xmlns:ns3="http://www.ebxml.org/namespaces/messageHeader"
	       xmlns:ns4="http://www.w3.org/1999/xlink" 
	xmlns:ns5="http://schemas.xmlsoap.org/ws/2002/12/secext">
	       <ns5:UsernameToken>
	         <ns5:Username>951852</ns5:Username>
	         <ns5:Password>WS986532</ns5:Password>
	         <Organization>WR17</Organization>
	         <Domain>DEFAULT</Domain>
	       </ns5:UsernameToken>
	     </ns5:Security>
	   </SOAP-ENV:Header>
	   <SOAP-ENV:Body>
	     <ns2:SessionCreateRQ xmlns:ns2="http://www.opentravel.org/OTA/2002/11">
	       <ns2:POS>
	         <ns2:Source/>
	       </ns2:POS>
	     </ns2:SessionCreateRQ>
	   </SOAP-ENV:Body>
	</SOAP-ENV:Envelope>"""

sabreCommand = """<?xml version="1.0" encoding="UTF-8"?>
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
      <SOAP-ENV:Header>
        <ns3:MessageHeader xmlns:ns2="http://www.w3.org/2000/09/xmldsig#"
          xmlns:ns3="http://www.ebxml.org/namespaces/messageHeader"
          xmlns:ns4="http://www.w3.org/1999/xlink" xmlns:ns5="http://schemas.xmlsoap.org/ws/2002/12/secext">
          <ns3:From>
            <ns3:PartyId>sample.url.of.sabre.client.com</ns3:PartyId>
          </ns3:From>
          <ns3:To>
            <ns3:PartyId>webservices.sabre.com</ns3:PartyId>
          </ns3:To>
          <ns3:CPAId>WR17</ns3:CPAId>
          <ns3:ConversationId>WR17-TERMINAL</ns3:ConversationId>
          <ns3:Service>SabreCommandLLSRQ</ns3:Service>
          <ns3:Action>SabreCommandLLSRQ</ns3:Action>
          <ns3:MessageData>
            <ns3:MessageId>somemessageid</ns3:MessageId>
            <ns3:Timestamp>Tue Sep 20 14:45:41 EDT 2016</ns3:Timestamp>
           <ns3:TimeToLive>2016-09-20T18:45:41.544Z</ns3:TimeToLive>
          </ns3:MessageData>
          <ns3:DuplicateElimination
            xmlns:xs="http://www.w3.org/2001/XMLSchema"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string"/>
          <ns3:Description>somedescription</ns3:Description>
        </ns3:MessageHeader>
        <ns5:Security xmlns:ns2="http://www.w3.org/2000/09/xmldsig#"
          xmlns:ns3="http://www.ebxml.org/namespaces/messageHeader"
          xmlns:ns4="http://www.w3.org/1999/xlink" xmlns:ns5="http://schemas.xmlsoap.org/ws/2002/12/secext">
          <ns5:BinarySecurityToken>%s</ns5:BinarySecurityToken>
          <ns2:group>WR17</ns2:group>
        </ns5:Security>
      </SOAP-ENV:Header>
      <SOAP-ENV:Body>
        <ns2:SabreCommandLLSRQ xmlns:ns2="http://webservices.sabre.com/sabreXML/2003/07">
          <ns2:Request CDATA="true" Output="SDS">
            <ns2:HostCommand>%s</ns2:HostCommand>
          </ns2:Request>
        </ns2:SabreCommandLLSRQ>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
    """

readItin ="""<?xml version="1.0" encoding="UTF-8"?>
        <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
          <SOAP-ENV:Header>
            <ns3:MessageHeader xmlns:ns2="http://www.w3.org/2000/09/xmldsig#"
              xmlns:ns3="http://www.ebxml.org/namespaces/messageHeader"
              xmlns:ns4="http://www.w3.org/1999/xlink" xmlns:ns5="http://schemas.xmlsoap.org/ws/2002/12/secext">
              <ns3:From>
                <ns3:PartyId>sample.url.of.sabre.client.com</ns3:PartyId>
              </ns3:From>
              <ns3:To>
                <ns3:PartyId>webservices.sabre.com</ns3:PartyId>
              </ns3:To>
              <ns3:CPAId>WR17</ns3:CPAId>
              <ns3:ConversationId>WR17-TERMINAL</ns3:ConversationId>
              <ns3:Service>TravelItineraryReadRQ</ns3:Service>
              <ns3:Action>TravelItineraryReadRQ</ns3:Action>
              <ns3:MessageData>
                <ns3:MessageId>somemessageid</ns3:MessageId>
                <ns3:Timestamp>Tue Sep 20 14:45:41 EDT 2016</ns3:Timestamp>
                <ns3:TimeToLive>2016-09-20T18:45:41.544Z</ns3:TimeToLive>
              </ns3:MessageData>
              <ns3:DuplicateElimination
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string"/>
              <ns3:Description>somedescription</ns3:Description>
            </ns3:MessageHeader>
            <ns5:Security xmlns:ns2="http://www.w3.org/2000/09/xmldsig#"
              xmlns:ns3="http://www.ebxml.org/namespaces/messageHeader"
              xmlns:ns4="http://www.w3.org/1999/xlink" xmlns:ns5="http://schemas.xmlsoap.org/ws/2002/12/secext">
              <ns5:BinarySecurityToken>%s</ns5:BinarySecurityToken>
              <ns2:group>WR17</ns2:group>
            </ns5:Security>
          </SOAP-ENV:Header>
          <SOAP-ENV:Body>
        <TravelItineraryReadRQ Version="3.8.0" TimeStamp="2012-09-19T10:00:00-06:00" xmlns="http://services.sabre.com/res/tir/v3_8" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dd="http://webservices.sabre.com/dd2">
            <MessagingDetails>
                <SubjectAreas>
                    <SubjectArea>FULL</SubjectArea>
                </SubjectAreas>
            </MessagingDetails>
            <UniqueID ID= '%s' />
            <EchoToken/>
        </TravelItineraryReadRQ>
          </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
        """
