Select 
	Access_code as  `access_code` 
  `activated`,
  `activator_company`,
  `activator_first_name`,
  `activator_last_name`,
  `comments`,
  `company_name`,
  `deployment`,
  `email`,
  `enabled`,
  `first_name`,
  `first_time_requested`,
  `host_id`,
  `hs_created_by_user_id`,  -- user that created the record
  `hs_createdate`,
  `hs_lastmodifieddate`,
  `hs_merged_object_ids`,
  `hs_updated_by_user_id`,  -- user that updated record
  `hubspot_owner_assigneddate`,  -- when owner assigned? can be blank omitted
  `hubspot_owner_id`, -- hubspot user that owns the record - via contact id ?
  `hubspot_team_id`, -- hubspot reference id
  `hs_object_id`,
  `last_name`,
  `last_time_requested`,
  `last_time_sent`,
  `license_expires_on`,
  `number_of_times_requested`,
  `number_of_times_sent`,
  `number_of_users`, 
  `record_id`,  -- hubspot reference id -- not primary key
  `requesting_email`,
  `status`,
  `technical_support_expires_on`,
  `unit_number`,
  `version_number`,
  `version_number_requested`
  
  from 9657_licenses_pemba_raw

