# -*- coding: utf-8 -*-

"""Classes for Route 53 domains."""

import uuid


class DomainManager:
	"""Manage an Route 53 domain."""

	def __init__(self, session):
		"""Create a DomainManager object."""
		self.session = session
		self.route53_client = self.session.client('route53')

	def find_hosted_zone(self, domain_name):
		"""Find zone matching domain name."""
		paginator = route53_client.get_paginator('list_hosted_zones')
		for page in paginator.paginate():
			for zone in page['HostedZones']:
				if domain_name.endswith(zone['Name'][:-1]):
					return zone

		return None
		
	def create_hosted_zone(self, domain_name):
		"""Create a hosted zone to match domain name."""
		zone_name = '.'.join(domain_name.split('.')[-2:]) + '.'
		return 	self.route53_client.create_hosted_zone(
			Name=zone_name,
			CallerReference=str(uuid.uuid4())
		)

	def create_s3_domain_record(self, zone, domain_name, endpoint):
		"""Create a domian record in zone for domain name."""
		return self.route53_client.change_resource_record_sets(
			HostedZoneId=zone['Id'],
			ChangeBatch={
				'Comment': 'Created by Webotron.',
				'Changes': [{
						'Action': 'UPSERT',
						'ResourceRecordSet': {
							'Name': domain_name,
							'Type': 'A',
							'AliasTarget': {
								'HostedZoneId': endpoint.zone,
								'DNSName': endpoint.host,
								'EvaluateTargetHealth': False
							}
						}
					}
				]
			}
		)