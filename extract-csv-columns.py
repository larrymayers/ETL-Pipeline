import csv
import pandas as pd

from decimal import Decimal, getcontext

def extract_values(input_file, output_file, columns_to_extract):
    df = pd.read_csv(input_file, usecols=columns_to_extract)
    df.to_csv(output_file, index=False)


# "Id","FirstName","LastName","Email","Phone","MemberId","LastBooking","NumberBookingsEver","NumberBookingLast30","FavoriteDay","FavoriteTime","NumberSpacesEver","NumberSpacesLast30",
# "EngagementScore","EngagementExplain","EngagementScoreLastMonth","EngagementExplainLastMonth","MerchantId","CreatedAt","Notes","StoredPaymentToken","StoredPaymentMask","ExportedToMailChimp",
# "DeletedAt","DoNotSendMessages","IsConcierge","PasswordSalt","PasswordResetGuid","PasswordResetExpires","HashedPassword","UserIdForPassword","UpdatedAt","Status","Token","CompanyId",
# "RelocityAgreementAttachments","RelocityInvoiceAttachments","RelocityWeeklyProgressAttachments","RelocityOverallProgressAttachments","RelocityComments","RelocityType","RelocityOccupancyType",
#  "RelocityMoveDate","RelocityTotalBudgeted","DataAnonymized","LatestEventBooking","LatestScheduleBooking","CombinedSearchField","RelocityDestinationCity","RelocityAreaId","RelocityRmcCustomerNumber",
# "RelocityRmcConsultantName","RelocityRmcConsultantEmail","Guid","Blocked","LastInvitedDate","SyncedWithThirdPartySystem"


# Product Type,Application ID,Applicant Type,Dsa Id,Dealer Id,Application Login Date,Application Status,Bank Name,HDB Branch Name,HDB Branch State,
# Queue Id,Current Stage,First Name,Middle Name,Last Name,DOB,Zip Code,City,State,Personal Mobile Number,Aadhar Verified,Credit Card Category,
# Approved Amount by CRO,Cibil Score,Mobile Verification,Margin Amount,Dealer Name,Total Asset Cost,Asset Ctg,Asset Model No,Los ID,Cro Remark 1,
# Applied Amount,Loyalty card No,Insurance Premium,EW Asset Category,Ew Warranty Tenure,Ew Warranty Premium,Primary Asset Category,Primary Asset Make,
# Primary Model No,Scheme Detail,Tenor,Finance Amount,Do Date,Serial Number/Imei Number,Serial No/Imei Status,Dealer Rank,Invoice Number,Invoice Date,
# Grid Id,Remark,Other Charges If Any,Personal Email Address,Permanent Email Address,Work Email Address,HIGHMARK SCORE,EMAIL VERIFICATION,E-NACH Flag
# Credit Rep_15_Feb_2023_01_02_45_348_HDB71518
# Usage example:
#for num in range(2, 49): | select -first 20
input_csv_file = f'./datasets/FlexBooker/Customers_202112231551.csv'
output_extracted_file = f'./datasets/FlexBooker/FlexBooker_Customers.csv'
columns_to_extract = ['Id', 'Email', 'FirstName', 'LastName', 'Phone', 'PasswordSalt', 'HashedPassword', 'UserIdForPassword']
#columns_to_extract = ['id','accountid','middle_name','conversationid','identityverified','referrerprofileid','stripe_customerid','city','email','price','phone','notes','flags','street','member','status','gender','logourl','gateway','twitter','website','country','balance','username','linkedin','postcode','location','facebook','longdesc','last_name','instagram','expertise','recruiter','shortdesc','language','lookingfor','crunchbase','first_name','timestamp','displayname','ycombinator','profiletype','relationship','interestedin','expirytimestamp','showdisplayname','lastactivitytime','push_notifications','verified_expertise','lastupdatetimestamp','birthdate_timestamp','lastmobiletimestamp','email_notifications']

extract_values(input_csv_file, output_extracted_file, columns_to_extract)

