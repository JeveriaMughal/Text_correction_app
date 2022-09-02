def closest_match(data):
    from fuzzywuzzy import fuzz
    score=1
    match=""
    for row in open("/run/user/1000/gvfs/sftp:host=192.168.18.17/home/j-mughal/Documents/data_pipeline/utils/text_files/ground_truth_record.txt","r"):
        score_tmp=fuzz.ratio(data,row)
        if score_tmp>= score:
            score=score_tmp
            match=row
    return match

def closest_match_multiple(data):
    from fuzzywuzzy import fuzz
    score=1
    match=[]
    for row in open("/run/user/1000/gvfs/sftp:host=192.168.18.17/home/j-mughal/Documents/data_pipeline/utils/text_files/ground_truth_record.txt","r"):
        score_tmp=fuzz.ratio(data,row)
        if score_tmp>= 72:
            match.append(row)
    return match
