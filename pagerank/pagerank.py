import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    prob_dict = {}

    # 如果当前页面没有链接到其他页面，则所有页面以相同概率被选中
    if len(corpus[page]) == 0:
        for p in corpus:
            prob_dict[p] = 1 / len(corpus)
        return prob_dict
    
    # 如果当前页面链接到其他页面，则有 damping_factor 的概率选择其中一个链接页面，有 1 - damping_factor 的概率选择所有页面
    for p in corpus:
        prob_dict[p] = (1 - damping_factor) / len(corpus)
    for p in corpus[page]:
        prob_dict[p] += damping_factor / len(corpus[page])
    return prob_dict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    cnt = {}
    for page in corpus:
        cnt[page] = 0
    start_page = random.choice(list(corpus.keys()))  # 随机选择一个页面作为起始页面
    cnt[start_page] += 1
    for i in range(n - 1):
        prob_dict = transition_model(corpus, start_page, damping_factor)
        start_page = random.choices(list(prob_dict.keys()), list(prob_dict.values()))[0]  # 根据概率分布随机选择一个页面
        cnt[start_page] += 1
    for page in cnt:
        cnt[page] /= n  # 除以总采样次数，得到每个页面的 PageRank 值
    return cnt


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    page_rank = {}
    for page in corpus:
        page_rank[page] = 1 / len(corpus)  # 初始化每个页面的 PageRank 值为 1 / N
    
    new_page_rank = {}
    flag = True
    while flag:
        flag = False
        for page in corpus:
            # 根据公式计算每个页面的 PageRank 值
            new_page_rank[page] = (1 - damping_factor) / len(corpus)
            for p in corpus:
                if page in corpus[p]:
                    if len(corpus[p]) == 0:  # 如果页面 p 没有链接到其他页面，则视为链接到所有页面
                        new_page_rank[page] += damping_factor * page_rank[p] / len(corpus)
                    else:
                        new_page_rank[page] += damping_factor * page_rank[p] / len(corpus[p])
            # 如果任意页面的 PageRank 值与上一次迭代相比，变化幅度大于 0.001，则继续迭代
            if abs(new_page_rank[page] - page_rank[page]) > 0.001:
                flag = True
        page_rank = new_page_rank.copy()
    
    return page_rank
        


if __name__ == "__main__":
    main()
