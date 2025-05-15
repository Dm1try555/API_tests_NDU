from faker import Faker

fake = Faker()

class Payloads:

    create_new_document= \
        {
            "documentType": "AccountOpeningOrder",
            "memberAccountReference": None,
            "memberDocumentNumber": None,
            "llcId": 3,
            "llcMemberType": "CATEGORY110"
        }
    

    change_document_by_id= \
        {
            "outNum": "test_outnum",
            "isPresentOutNum": True,
            "outDate": "2025-05-15T18:47:57.923Z",
            "llcMemberType": "CATEGORY110",
            "shareSize": 0,
            "isFullShareSize": True,
            "capitalShareAction": "Buy",
            "counterPartyCode": "test_counterpartycode",
            "counterPartyName": "test_counterpartyname",
            "nameBlockFor": "test_nameblockfor",
            "codeBlockFor": "test_codeblockfor",
            "blockReasonNameOther": "test_blockreasonnameother",
            "escrowAccountNumber": "test_escrowaccountnumber",
            "escrowDocumentNumber": "test_escrowdocumentnumber",
            "escrowDocumentDate": "2025-05-15T18:47:57.923Z",
            "contractNum": "test_contractnum",
            "contractDate": "2025-05-15T18:47:57.923Z",
            "messageCdData": "test_messagecdData",
            "messageCdTopic": "test_messagecdtopic",
            "messageCdFileUrl": "test_messagecdfileurl",
            "p_Surname": "test_surname",
            "p_Name": "test_name",
            "p_Secondname": "test_secondname",
            "p_Code": "test_code",
            "p_IsCodeExist": True,
            "p_CodeEDDR": "test_codeeddr",
            "p_Citizenship": "test_citizenship",
            "p_BirthPlace": "test_birthplace",
            "p_DocumentName": "test_documentname",
            "p_DocumentNumber_Series": "test_documentnumberseries",
            "p_DocumentNumber": "test_documentnumber",
            "p_DocumentDate": "2025-05-15T18:47:57.924Z",
            "p_DocumentWho": "test_documentwho",
            "p_BirthDate": "2025-05-15T18:47:57.924Z",
            "p_Country": "test_country",
            "p_Region": "test_region",
            "p_City": "test_city",
            "p_Address": "test_address",
            "p_PostIndex": "test_postindex",
            "p_Is_Mailing_Address_Matches_Location": True,
            "p_CodeTerUnit": "test_codeterunit",
            "p_TaxResidencyStatusResName": True,
            "p_IsFOP": True,
            "p_FOPAuthority": "test_fopauthority",
            "p_PostAddress": "test_postaddress",
            "p_Phone": "test_phone",
            "p_MobilePhone": "test_mobilephone",
            "p_Email": "test_email",
            "p_EmailSend": "test_emailsend",
            "p_BankName": "test_bankname",
            "p_BankMFO": "test_bankmfo",
            "p_BankAccount": "test_bankaccount",
            "p_ContractNum": "test_contractnum",
            "p_ContractDate": "2025-05-15T18:47:57.924Z",
            "mg_Name": "test_mgname",
            "mg_Code": "test_mgcode",
            "mg_IsJur": True,
            "mg_AuthDocument": "test_mgauthdocument",
            "mg_TermAuthority": "test_mgtermauthority",
            "mg_DocumentNumber_Series": "test_mgdocumentnumberseries",
            "mg_DocumentNumber": "test_mgdocumentnumber",
            "firstPersonName": "test_firstpersonname",
            "firstPersonCode": "test_firstpersoncode",
            "firstPersonCode_DocumentNumber_Series": "test_firstpersoncodedocumentnumberseries",
            "firstPersonCode_DocumentNumber": "test_firstpersoncodedocumentnumber",
            "firstPersonPosition": "test_firstpersonposition",
            "f_DocumentInfo": "test_fdocumentinfo",
            "f_TermAuthority": "test_ftermauthority",
            "jurNonResidentName": "test_jurnonresidentname",
            "jurNonResidentShortName": "test_jurnonresidentshortname",
            "jurNonResidentCode": "test_jurnonresidentcode",
            "jurNonResidentRegCountry": "test_jurnonresidentregcountry",
            "p_TaxResidencyStatusResOwnersName": True,
            "jurName": "test_jurname",
            "jurShortName": "test_jurshortname",
            "jurShortNameEng": "test_jurshortnameeng",
            "jurEdrpou": "test_juredrpou",
            "jurEdrisi": "test_juredrisi",
            "jurRegCountry": "test_jurregcountry",
            "govName": "test_govname",
            "govShortName": "test_govshortname",
            "govCode": "test_govcode",
            "managerList": [
                {
                "m_Name": "test_mname",
                "m_Code": "test_mcode",
                "m_DocumentName": "test_mdocumentname",
                "m_DocumentSerial": "test_mdocumentserial",
                "m_DocumentNumber": "test_mdocumentnumber",
                "m_DocumentDate": "2025-05-15T18:47:57.924Z",
                "m_DocumentWho": "test_mdocumentwho",
                "m_AuthDocument": "test_mauthdocument",
                "m_TermAuthority": "2025-05-15T18:47:57.924Z"
                }
            ],
            "representList": [
                {
                "r_Code": "test_rcode",
                "r_Name": "test_rname",
                "r_DocumentSeria": "test_rdocumentseria",
                "r_DocumentNumber": "test_rdocumentnumber",
                "r_DocumentDate": "2025-05-15T18:47:57.924Z",
                "r_DocumentWho": "test_rdocumentwho",
                "r_AuthDocument": "test_rauthdocument",
                "r_DocumentName": "test_rdocumentname",
                "r_TermAuthority": "2025-05-15T18:47:57.924Z",
                "r_Email": "test_remail",
                "r_Phone": "test_rphone",
                "r_AuthAuthority": "test_rauthauthority"
                }
            ]
        }


