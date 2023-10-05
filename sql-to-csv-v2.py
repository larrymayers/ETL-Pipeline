import re
import csv

def sanitize_string(text):
    # Remove non-ASCII characters
    sanitized = re.sub(r'[^\x00-\x7F]+', '', text)
    return sanitized

def is_email(line):
    # Check if the line starts with an email address
    return re.match(r'^\S+@\S+', line) is not None

def convert_to_csv(input_file, output_file, garbage_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        input_text = infile.read()
    
    lines = input_text.strip().split('\n')
    csv_rows = []
    garbage_lines = []

    for line in lines:
        if is_email(line):
            columns = line.split('\t')
            columns = [sanitize_string(col) for col in columns]
            
            if len(columns) >= 15:  # Change to 15 columns (adjust as needed)
                id, email, first_name, last_name, created_at, updated_at, blaze, dynamo, steel, tempo, questions_completed, questions_completed_at, personality_type, step_1_complete, step_2_complete, step_3_complete, step_4_complete, step_5_complete, step_6_complete, step_7_complete, step_8_complete, step_9_complete, step_10_complete, strengths, skills, user_likes, social_score, share_count, twitter_name, linkedin_url, google_plus_url, wd_profile, celebrity, celebrity_url, about, ranked, regal, allows_marketing, invitee, confirmed_details, image_url, gender, location, encrypted_password, reset_password_token, reset_password_sent_at, remember_created_at, sign_in_count, current_sign_in_at, last_sign_in_at, current_sign_in_ip, last_sign_in_ip, authentication_token, spectrum_level, mmp_token, passion_test_taken_at, old_passions, added_to_gt_users_crm, salesforce_updated, salesforce_failed, passion_affiliate, passion_affiliate_set_at, crystal_circle, downloaded_genius_guide, wealth_dynamics_report_url, td_profile, td_report_url, send_message_notifications, send_friend_notifications, about_mentor, avatar_file_name, avatar_content_type, avatar_file_size, avatar_updated_at, url_imported, salesforce_id, full_name, wd_profile_locked, clerk, tsv, scholar, ilab, passion_fixed, purpose_id, purpose_test_taken_at, in_beta, mentor, average_rating, ranking, accelerator, send_comment_notifications, balance_cents, user_type, title, short_description, genie_id, emc, apprentice_interested, website_link, auto_responder, fb_url, accelerator_mission, send_ebc_notification, send_ei_partners_notification, send_entrepreneur_inspiration_notification, send_ffyb_notification, send_impact_investors_notification, send_geniusu_notification, send_hd_notification, send_genius_school_notification, location_term_condition, is_onboard, send_real_estate_investment, leader, send_event_create_notifications, tsv_name, tsv_location, tsv_about, discarded_at, latitude, longitude, send_circle_invite_notifications, country_from_ip, uuid, sf_updated_at, confirmation_token, confirmed_at, confirmation_sent_at, unconfirmed_email, force_confirmation = columns

                # Handle missing or empty name parts
                name_parts = full_name.split(' ', 2)
                if len(name_parts) == 3:
                    firstname, middlename, lastname = name_parts
                elif len(name_parts) == 2:
                    firstname, lastname = name_parts
                    middlename = ''
                else:
                    firstname, middlename, lastname = '', '', ''

                csv_row = [
                    id, email, first_name, last_name, created_at, updated_at, blaze, dynamo, steel, tempo,
                    questions_completed, questions_completed_at, personality_type, step_1_complete, step_2_complete,
                    step_3_complete, step_4_complete, step_5_complete, step_6_complete, step_7_complete,
                    step_8_complete, step_9_complete, step_10_complete, strengths, skills, user_likes,
                    social_score, share_count, twitter_name, linkedin_url, google_plus_url, wd_profile, celebrity,
                    celebrity_url, about, ranked, regal, allows_marketing, invitee, confirmed_details, image_url,
                    gender, location, encrypted_password, reset_password_token, reset_password_sent_at,
                    remember_created_at, sign_in_count, current_sign_in_at, last_sign_in_at, current_sign_in_ip,
                    last_sign_in_ip, authentication_token, spectrum_level, mmp_token, passion_test_taken_at,
                    old_passions, added_to_gt_users_crm, salesforce_updated, salesforce_failed, passion_affiliate,
                    passion_affiliate_set_at, crystal_circle, downloaded_genius_guide, wealth_dynamics_report_url,
                    td_profile, td_report_url, send_message_notifications, send_friend_notifications, about_mentor,
                    avatar_file_name, avatar_content_type, avatar_file_size, avatar_updated_at, url_imported,
                    salesforce_id, full_name, wd_profile_locked, clerk, tsv, scholar, ilab, passion_fixed, purpose_id,
                    purpose_test_taken_at, in_beta, mentor, average_rating, ranking, accelerator,
                    send_comment_notifications, balance_cents, user_type, title, short_description, genie_id,
                    emc, apprentice_interested, website_link, auto_responder, fb_url, accelerator_mission,
                    send_ebc_notification, send_ei_partners_notification, send_entrepreneur_inspiration_notification,
                    send_ffyb_notification, send_impact_investors_notification, send_geniusu_notification,
                    send_hd_notification, send_genius_school_notification, location_term_condition, is_onboard,
                    send_real_estate_investment, leader, send_event_create_notifications, tsv_name, tsv_location,
                    tsv_about, discarded_at, latitude, longitude, send_circle_invite_notifications, country_from_ip,
                    uuid, sf_updated_at, confirmation_token, confirmed_at, confirmation_sent_at, unconfirmed_email,
                    force_confirmation
                ]
                csv_rows.append(csv_row)
            else:
                print(f"Skipping line in CSV: {line}")
        else:
            # Lines that don't start with an email address go to the garbage file
            garbage_lines.append(line)
    
    # Write to CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([
            'id', 'email', 'first_name', 'last_name', 'created_at', 'updated_at', 'blaze', 'dynamo', 'steel',
            'tempo', 'questions_completed', 'questions_completed_at', 'personality_type', 'step_1_complete',
            'step_2_complete', 'step_3_complete', 'step_4_complete', 'step_5_complete', 'step_6_complete',
            'step_7_complete', 'step_8_complete', 'step_9_complete', 'step_10_complete', 'strengths', 'skills',
            'user_likes', 'social_score', 'share_count', 'twitter_name', 'linkedin_url', 'google_plus_url',
            'wd_profile', 'celebrity', 'celebrity_url', 'about', 'ranked', 'regal', 'allows_marketing', 'invitee',
            'confirmed_details', 'image_url', 'gender', 'location', 'encrypted_password', 'reset_password_token',
            'reset_password_sent_at', 'remember_created_at', 'sign_in_count', 'current_sign_in_at',
            'last_sign_in_at', 'current_sign_in_ip', 'last_sign_in_ip', 'authentication_token', 'spectrum_level',
            'mmp_token', 'passion_test_taken_at', 'old_passions', 'added_to_gt_users_crm', 'salesforce_updated',
            'salesforce_failed', 'passion_affiliate', 'passion_affiliate_set_at', 'crystal_circle',
            'downloaded_genius_guide', 'wealth_dynamics_report_url', 'td_profile', 'td_report_url',
            'send_message_notifications', 'send_friend_notifications', 'about_mentor', 'avatar_file_name',
            'avatar_content_type', 'avatar_file_size', 'avatar_updated_at', 'url_imported', 'salesforce_id',
            'full_name', 'wd_profile_locked', 'clerk', 'tsv', 'scholar', 'ilab', 'passion_fixed', 'purpose_id',
            'purpose_test_taken_at', 'in_beta', 'mentor', 'average_rating', 'ranking', 'accelerator',
            'send_comment_notifications', 'balance_cents', 'user_type', 'title', 'short_description', 'genie_id',
            'emc', 'apprentice_interested', 'website_link', 'auto_responder', 'fb_url', 'accelerator_mission',
            'send_ebc_notification', 'send_ei_partners_notification', 'send_entrepreneur_inspiration_notification',
            'send_ffyb_notification', 'send_impact_investors_notification', 'send_geniusu_notification',
            'send_hd_notification', 'send_genius_school_notification', 'location_term_condition', 'is_onboard',
            'send_real_estate_investment', 'leader', 'send_event_create_notifications', 'tsv_name', 'tsv_location',
            'tsv_about', 'discarded_at', 'latitude', 'longitude', 'send_circle_invite_notifications',
            'country_from_ip', 'uuid', 'sf_updated_at', 'confirmation_token', 'confirmed_at',
            'confirmation_sent_at', 'unconfirmed_email', 'force_confirmation'
        ])
        csv_writer.writerows(csv_rows)

    # Write garbage lines to the garbage file
    with open(garbage_file, 'w', encoding='utf-8') as garbage_file:
        garbage_file.write('\n'.join(garbage_lines))

#input_file_path = 'input.txt'    # Replace with the path to your input file
#output_file_path = 'output.csv'  # Replace with the desired output file path



input_file_path = r".\datasets\Geniusu\chunks\geniusu_00000001.csv"    # Replace with the path to your input file
output_file_path = r".\datasets\Geniusu\geniusu_1_output.csv"  # Replace with the desired output file path
garbage_file_path = r".\datasets\Geniusu\geniusu_1_garbage.txt"  # Replace with the path to the garbage file

# folder_path = r".\datasets\Aptoide.com\chunks\\"
# output_folder = r".\datasets\Aptoide.com\\"

# for number in range(100, 137):  # Loop through numbers 32 to 132 (inclusive)
#     input_file_path = f"{folder_path}aptoide_00000{number}.txt"
#     output_file_path = f"{output_folder}aptoide_{number}.csv"
#     convert_to_csv(input_file_path, output_file_path)

convert_to_csv(input_file_path, output_file_path, garbage_file_path)
