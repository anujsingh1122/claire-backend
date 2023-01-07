from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/membership'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Membership(db.Model):
    reference_number = db.Column(db.String(45), primary_key=True)
    companyName = db.Column(db.String(100), nullable=False)
    memberType = db.Column(db.String(20), nullable=False)
    currentOrLapsed = db.Column(db.String(2), nullable=False)
    sicCode = db.Column(db.String(100), nullable=True)
    sector = db.Column(db.String(200), nullable=True)
    mainSector = db.Column(db.String(200), nullable=True)
    # accountsFiled = db.Column(db.String(1), nullable=True)
    # isContractSigned = db.Column(db.String(1), nullable=True)
    # isDowCopUser = db.Column(db.String(1), nullable=True)
    # mainContact = db.Column(db.String(50), nullable=True)
    # contactEmail = db.Column(db.String(100), nullable=True)
    # contactAddressLine1 = db.Column(db.String(100), nullable=True)
    # contactAddressPostCode = db.Column(db.String(10), nullable=True)
    # contactTelephone = db.Column(db.String(50), nullable=True)
    # invoiceNum = db.Column(db.String(50), nullable=True)
    # invoiceAmt = db.Column(db.String(15), nullable=True)
    # reminderDate = db.Column(db.Date, nullable=True)
    # dateReceived = db.Column(db.Date, nullable=True)
    # paymentDate = db.Column(db.Date, nullable=True)
    # membershipYear = db.Column(db.String(4), nullable=True)
    # isCertificateSent = db.Column(db.String(1), nullable=True)
    # connectMethod = db.Column(db.String(100), nullable=True)
    # logoRequested = db.Column(db.String(3), nullable=True)
    # websitePresence = db.Column(db.String(1), nullable=True)
    # linkedInHandle = db.Column(db.String(100), nullable=True)
    # twitterHandle = db.Column(db.String(100), nullable=True)
    # notes = db.Column(db.Text, nullable=True)
    # claireResponsible = db.Column(db.String(45), nullable=True)
    # membership_renewal = db.Column(db.Date, nullable=True)
    # claire_contact = db.Column(db.String(45), nullable=True)
    # companyNumber = db.Column(db.Integer, nullable=True)
    # registeredAddressLine1 = db.Column(db.String(45), nullable=True)
    # registeredAddressLine2 = db.Column(db.String(45))
    # registeredAddressLine3 = db.Column(db.String(45))
    # registeredAddressLocality = db.Column(db.String(45))
    # registeredAddressRegion = db.Column(db.String(45))
    # registeredAddressCountry = db.Column(db.String(45))
    # contactAddressLine2 = db.Column(db.String(45))
    # contactAddressLine3 = db.Column(db.String(45))
    # contactAddressLocality = db.Column(db.String(45))
    # contactAddressRegion = db.Column(db.String(45))
    # contactAddressCountry = db.Column(db.String(45))
    # registeredAddressPostCode = db.Column(db.String(45))
    # acctLastMadeUpto = db.Column(db.Date)
    # confStmtLastMadeUpto = db.Column(db.Date)


@app.route('/', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
# @cross_origin(origin='*',headers=['Content-Type'])
def handle_members():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_member = Membership(reference_number=data['reference_number'], companyName=data['companyName'],
                                    memberType=data['memberType'], currentOrLapsed=data['currentOrLapsed'],
                                    sicCode=data['sicCode'], sector=data['sector'], mainSector=data['mainSector'],
                                    # accountsFiled=data['accountsFiled'], isContractSigned=data['isContractSigned'],
                                    # isDowCopUser=data['isDowCopUser'], mainContact=data['mainContact'],
                                    # contactEmail=data['contactEmail'], contactAddressLine1=data['contactAddressLine1'],
                                    # contactAddressPostCode=data['contactAddressPostCode'],
                                    # contactTelephone=data['contactTelephone'], invoiceNum=data['invoiceNum'],
                                    # invoiceAmt=data['invoiceAmt'], reminderDate=data['reminderDate'],
                                    # dateReceived=data['dateReceived'], paymentDate=data['paymentDate'],
                                    # membershipYear=data['membershipYear'], isCertificateSent=data['isCertificateSent'],
                                    # connectMethod=data['connectMethod'], logoRequested=data['logoRequested'],
                                    # websitePresence=data['websitePresence'], linkedInHandle=data['linkedInHandle'],
                                    # twitterHandle=data['twitterHandle'], notes=data['notes'],
                                    # claireResponsible=data['claireResponsible'],
                                    # membership_renewal=['membership_renewal'],
                                    # claire_contact=data['claire_contact'], companyNumber=data['companyNumber'],
                                    # registeredAddressLine1=data['registeredAddressLine1'],
                                    # registeredAddressLine2=data['registeredAddressLine2'],
                                    # registeredAddressLine3=data['registeredAddressLine3'],
                                    # registeredAddressLocality=data['registeredAddressLocality'],
                                    # registeredAddressRegion=data['registeredAddressRegion'],
                                    # registeredAddressCountry=data['registeredAddressCountry'],
                                    # contactAddressLine2=data['contactAddressLine2'],
                                    # contactAddressLine3=data['contactAddressLine3'],
                                    # contactAddressLocality=data['contactAddressLocality'],
                                    # contactAddressRegion=data['contactAddressRegion'],
                                    # contactAddressCountry=data['contactAddressCountry'],
                                    # registeredAddressPostCode=data['registeredAddressPostCode'],
                                    # acctLastMadeUpto=data['acctLastMadeUpto'],
                                    # confStmtLastMadeUpto=data['confStmtLastMadeUpto'],

                                    )
            db.session.add(new_member)
            db.session.commit()
            return {"message": f" {new_member.reference_number} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        members = Membership.query.all()
        results = [
            {
                "reference_number": member.reference_number,
                "companyName": member.companyName,
                "memberType": member.memberType,
                "currentOrLapsed": member.currentOrLapsed,
                "sicCode": member.sicCode,
                "sector": member.sector,
                "mainSector": member.mainSector,
                # "accountsFiled": member.accountsFiled,
                # "isContractSigned": member.isContractSigned,
                # "isDowCopUser": member.isDowCopUser,
                # "mainContact": member.mainContact,
                # "contactEmail": member.contactEmail,
                # "contactAddressLine1": member.contactAddressLine1,
                # "contactAddressPostCode": member.contactAddressPostCode,
                # "contactTelephone": member.contactTelephone,
                # "invoiceNum": member.invoiceNum,
                # "invoiceAmt": member.invoiceAmt,
                # "reminderDate": member.reminderDate,
                # "dateReceived": member.dateReceived,
                # "paymentDate": member.paymentDate,
                # "membershipYear": member.membershipYear,
                # "isCertificateSent": member.isCertificateSent,
                # "connectMethod": member.connectMethod,
                # "logoRequested": member.logoRequested,
                # "websitePresence": member.websitePresence,
                # "linkedInHandle": member.linkedInHandle,
                # "twitterHandle": member.twitterHandle,
                # "notes": member.notes,
                # "claireResponsible": member.claireResponsible,
                # "membership_renewal": member.membership_renewal,
                # "claire_contact": member.claire_contact,
                # "companyNumber": member.companyNumber,
                # "registeredAddressLine1": member.registeredAddressLine1,
                # "registeredAddressLine2": member.registeredAddressLine2,
                # "registeredAddressLine3": member.registeredAddressLine3,
                # "registeredAddressLocality": member.registeredAddressLocality,
                # "registeredAddressRegion": member.registeredAddressRegion,
                # "registeredAddressCountry": member.registeredAddressCountry,
                # "contactAddressLine2": member.contactAddressLine2,
                # "contactAddressLine3": member.contactAddressLine3,
                # "contactAddressLocality": member.contactAddressLocality,
                # "contactAddressRegion": member.contactAddressRegion,
                # "contactAddressCountry": member.contactAddressCountry,
                # "registeredAddressPostCode": member.registeredAddressPostCode,
                # "acctLastMadeUpto": member.acctLastMadeUpto,
                # "confStmtLastMadeUpto": member.confStmtLastMadeUpto,
            } for member in members]

        # return {"count": len(results), "members": results}
        return results


if __name__ == '__main__':
    app.run(debug=True)
