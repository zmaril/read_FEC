# How many races have multiple candidates raising big sums of money?
import sys, os

from django.core.management import setup_environ
sys.path.append('../fecreader/')
sys.path.append('../')

import settings
setup_environ(settings)

from summary_data.models import District, Candidate_Overlay

fundraising_threshold = 100000

for office in ['H', 'S']:
    # Ignore open seats
    races = District.objects.filter(office=office, open_seat=False)

    for race in races:
        credible_candidates = Candidate_Overlay.objects.filter(district=race, total_receipts__gte=fundraising_threshold).exclude(not_seeking_reelection=True)
        if len(credible_candidates) > 1:
            print "\n\nFound multiple candidates in district %s %s %s -- Rating is: %s incumbent is %s %s " % (race.state, race.office, race.office_district, race.rothenberg_rating_text, race.incumbent_name, race.incumbent_party)
            for challenger in credible_candidates:
                print "\tcandidate: |%s| (|%s|) total_receipts|%s| cash:|%s| as of|%s|" % (challenger.name, challenger.party, challenger.total_receipts, challenger.cash_on_hand, challenger.cash_on_hand_date)