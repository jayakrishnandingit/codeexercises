#/usr/bin/python3
import os
import re
import datetime

import requests
from dataclasses import dataclass, field
from collections import Counter

GITHUB_TOKEN = os.environ.get('GITHUB_FINE_GRAINED_TOKEN')
HEADERS = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {GITHUB_TOKEN}',
    'X-GitHub-Api-Version': '2022-11-28'
}


@dataclass
class RepoEvent(object):
    pk: int
    ref: str
    timestamp: str
    activity_type: str
    actor: str



@dataclass
class Labels(object):
    pk: int
    name: str
    color: str


@dataclass
class PullRequest(object):
    url: str
    number: int
    state: str
    title: str
    draft: bool
    user: str
    labels: list[Labels]
    created_at: datetime.datetime = field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = field(default_factory=datetime.datetime.utcnow)


def get_pull_requests(repo: str, state: str = 'open', page: int = 1) -> list:
    """
    A function to get all PRs in a particular state(open, close, all) in a repo.
    This function will handle pagination and get all records.
    """
    data = []
    print(f'Getting page {page}.')
    response = requests.get(
        f'https://api.github.com/repos/hellofresh/{repo}/pulls?state={state}&page={page}',
        headers=HEADERS
    )
    for r in response.json():
        data.append(
            PullRequest(
                url=r['url'],
                number=r['number'],
                state=r['state'],
                title=r['title'],
                draft=r['draft'],
                user=r['user']['login'],
                labels=[Labels(pk=l['id'], name=l['name'], color=l['color']) for l in r['labels']],
                created_at=r['created_at'],
                updated_at=r['updated_at']
            )
        )
    yield data

    link_header = response.headers.get('Link')

    if link_header is not None and 'rel="next"' in link_header:
        next_page = re.search('page=(\d+)(?=>;\srel="next")', link_header)
        if next_page:
            next_page = next_page.group(1)

            yield from get_pull_requests(repo, state, next_page)


def get_pr_label_stats(repo: str, state: str = 'open'):
    """
    A function to count the number of distinct labels used in all PRs in a repo.
    """
    labels_counter = Counter()
    for prs in get_pull_requests(repo, state):
        for pr in prs:
            labels_counter.update([l.name for l in pr.labels])
    return labels_counter
        

if __name__ == '__main__':
    print(get_pr_label_stats(repo='td-workflows', state='all'))

