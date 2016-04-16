# helper functions for the script that is supposed to help fix the hhs marketplace dataset
def checkRow(record):
    # enter "NULL" for emply fields (e.g.,'') and "NA" instead of "X" for data that was not provided by the plan
    tmp = [x if x != "" else "NA" for x in record]
    newRow = [x if x != "X" else "NA" for x in tmp]
    return newRow

def checkCols(record):
    if len(record) == 21: return 1
    else:
        print record
        return 0

def planType(planinfo):
    # "Y" indicates only dentalcoverage
    # "N" is a health plan that may include dental
    if planinfo =="Y": return "dental"
    if planinfo =="N": return "health"
    else:
        print "BAD VALUE:",planinfo
        return planinfo

def stateField(statestatus):
    # one and multi-state plans
    if statestatus =="Y": return "multiState"
    if statestatus =="N": return "stateLevel"
    if statestatus =="NA": return statestatus
    else:
        print "BAD VALUE:",statestatus
        return statestatus

def adultChild(adultchildstatus):
    # types of child and adult coverage
    if adultchildstatus =="0": return "adultsAndKids"
    if adultchildstatus =="1": return "childOnly"
    if adultchildstatus =="2": return "adultOnly"
    if adultchildstatus =="NA": return adultchildstatus
    else:
        print "BAD VALUE:", adultchildstatus
        return adultchildstatus

def wholeCtyCheck(zipcode):
    # value "00000" indicates that all zips in the county are covered
    if zipcode =="00000" or zipcode == "0": return "wholeCnty"
    else: return zipcode

def crosswalkLevel(xlevel):
    # crosswalk levels
    if xlevel =="0": return "xSamePlan"
    if xlevel =="1": return "xPlanLevel"
    if xlevel =="2": return "xPlanCnty"
    if xlevel =="3": return "xZipcode"
    if xlevel =="4": return "xDiscontinued"
    if xlevel =="5": return "xWithdrawn"
    if xlevel == "NA": return xlevel
    else:
        print "BAD VALUE:", xlevel
        return xlevel

def crosswalkReason(xreas):
    # reasons for the crosswalk
    if xreas =="0": return "renewingSamePlan" # reason
    if xreas =="1": return "renewingDiffPlan"
    if xreas =="2": return "renewingProduct"
    if xreas =="3": return "continuingPlan"
    if xreas =="4": return "continuingProduct"
    if xreas =="5": return "discontNoOpt"
    if xreas =="6": return "discontProduct"
    if xreas == "NA": return xreas
    else:
        print "BAD VALUE:", xreas
        return xreas

def planIDCheck(planid):
    # value "00000XX0000000" means discontinued with no auto-enrollment   
    if planid == '00000XX0000000': return "discontinued"
    else: return planid

def issuerIDCheck(issueID):
    # value "00000" means discontinued with no auto-enrollment
    if issueID == "00000" or issueID == "0": return "discontinued"
    else: return issueID

def ageOffIDCheck(ageoffid):
    # value "00000XX0000000" measns that field was not provided  
    if ageoffid == '00000XX0000000': return "NA"
    else: return ageoffid
    
def ageoffIssuerIDCheck(ageoffid):
    # value "00000" measns that field was not provided
    if ageoffid == "00000" or ageoffid == "0": return "NA"
    else: return ageoffid

        # product/plan combination using the same 2015 Plan ID; a value of 1 equals Renewing the same product/plan combination using a different 2016 Plan ID; a value of 2 equals Renewing product or renewal in a different plan within the product; a value of 3 equals Continuing product with no plan available in the particular service area under that product and enrollment in a different product; a value of 4 equals Continuing product with no plan available in the particular service area under that product and no enrollment option; a value of 5 equals Discontinuing product and no enrollment option; a value of 6 equals Discontinuing
        # A value of 0 equals Crosswalking to the same Plan ID; a value of 1 equals Crosswalking at the Plan ID level; a value of 2 equals Crosswalking at the Plan ID and county coverage level; a value of 3 equals Crosswalking at the zip-code level for one or more counties; a value of 4 equals Discontinue 2015 plan with no cross walk (no re-enrollment option in 2016); a value of 5 equals 2015 Plan withdrawn prior to certificatio
