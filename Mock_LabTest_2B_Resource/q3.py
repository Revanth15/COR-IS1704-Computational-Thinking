def count_emails(file_name, start_time, end_time, sender):
    # Modify the code below.
    valid_count = 0
    with open(file_name, 'r') as file:
        for line in file:
            time_stamp, sendr, recipient = line.strip().split("\t")
            if sendr != sender:
                continue
            
            # time stamp adjustment
            time_stamp_elements = time_stamp.split(":")
            hr = int(time_stamp_elements[0])
            mins = int(time_stamp_elements[1])
            secs = int(time_stamp_elements[2][0:2])

            start_hr, start_min = start_time
            end_hr, end_min = end_time
            if time_stamp_elements[2].endswith("PM"):
                if hr != 12:
                    hr += 12
            elif time_stamp_elements[2].endswith("AM"):
                if hr == 12:
                    hr -= 12

            time_stamp_secs = (hr * 60 * 60) + (mins * 60) + secs
            start_time_stamp_secs = (start_hr * 60 * 60) + (start_min * 60)
            end_time_stamp_secs = (end_hr * 60 * 60) + (end_min * 60)

            if start_time_stamp_secs <= time_stamp_secs <= end_time_stamp_secs:
                valid_count += 1

    return valid_count    
