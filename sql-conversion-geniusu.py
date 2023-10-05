import csv

folder_path = r".\datasets\Geniusu\chunks\\"

### For loop required
for number in range(12,49):
    # Define the input and output file paths
    input_file_path = f"{folder_path}geniusu_{number:08}.csv" # Replace with your input file path
    output_file_path = f"{folder_path}geniusu_{number}.csv"  # Replace with your desired output file path

    # Create the header for the CSV
    header = [
        "id", "email", "first_name", "last_name", "created_at", "updated_at", "blaze", "dynamo", "steel", "tempo", "questions_completed",
        "questions_completed_at", "personality_type", "step_1_complete", "step_2_complete", "step_3_complete", "step_4_complete",
        "step_5_complete", "step_6_complete", "step_7_complete", "step_8_complete", "step_9_complete", "step_10_complete", "strengths",
        "skills", "user_likes", "social_score", "share_count", "twitter_name", "linkedin_url", "google_plus_url", "wd_profile", "celebrity",
        "celebrity_url", "about", "ranked", "regal", "allows_marketing", "invitee", "confirmed_details", "image_url", "gender", "location",
        "encrypted_password", "reset_password_token", "reset_password_sent_at", "remember_created_at", "sign_in_count", "current_sign_in_at",
        "last_sign_in_at", "current_sign_in_ip", "last_sign_in_ip", "authentication_token", "spectrum_level", "mmp_token", "passion_test_taken_at",
        "old_passions", "added_to_gt_users_crm", "salesforce_updated", "salesforce_failed", "passion_affiliate", "passion_affiliate_set_at",
        "crystal_circle", "downloaded_genius_guide", "wealth_dynamics_report_url", "td_profile", "td_report_url", "send_message_notifications",
        "send_friend_notifications", "about_mentor", "avatar_file_name", "avatar_content_type", "avatar_file_size", "avatar_updated_at",
        "url_imported", "salesforce_id", "full_name", "wd_profile_locked", "clerk", "tsv", "scholar", "ilab", "passion_fixed", "purpose_id",
        "purpose_test_taken_at", "in_beta", "mentor", "average_rating", "ranking", "accelerator", "send_comment_notifications",
        "balance_cents", "user_type", "title", "short_description", "genie_id", "emc", "apprentice_interested", "website_link",
        "auto_responder", "fb_url", "accelerator_mission", "send_ebc_notification", "send_ei_partners_notification",
        "send_entrepreneur_inspiration_notification", "send_ffyb_notification", "send_impact_investors_notification", "send_geniusu_notification",
        "send_hd_notification", "send_genius_school_notification", "location_term_condition", "is_onboard", "send_real_estate_investment",
        "leader", "send_event_create_notifications", "tsv_name", "tsv_location", "tsv_about", "discarded_at", "latitude", "longitude",
        "send_circle_invite_notifications", "country_from_ip", "uuid", "sf_updated_at", "confirmation_token", "confirmed_at",
        "confirmation_sent_at", "unconfirmed_email", "force_confirmation"
    ]

    # Create the output CSV file and write the header
    with open(output_file_path, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)

        # Read the input file line-by-line and write each line to the output CSV
        with open(input_file_path, "r", encoding="utf-8") as infile:
            for line in infile:
                data = line.strip().split("\t")
                if len(data) == len(header):
                    # Replace missing data with empty strings
                    data = [field if field != "\\N" else "" for field in data]
                    # Ensure proper UTF-8 encoding for each field
                    data = [field.encode("utf-8", "ignore").decode("utf-8") for field in data]
                    csv_writer.writerow(data)

print("CSV file created:", output_file_path)
