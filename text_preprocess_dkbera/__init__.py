from text_preprocess_dkbera import utils

__version__ = '0.0.6'


def get_wordcounts(x):
	return utils._get_wordcounts(x)

def get_charcounts(x):
	return utils._get_charcounts(x)

def get_avg_wordlength(x):
	return utils._get_avg_wordlength(x)

def get_stopword_counts(x):
	return utils._get_stopword_counts(x)

def get_hastag_counts(x):
	return utils._get_hastag_counts(x)

def get_mention_counts(x):
	return utils._get_mention_counts(x)

def get_degit_counts(x):
	return utils._get_degit_counts(x)

def get_uppercase_counts(x):
	return utils._get_uppercase_counts(x)

def cont_exp(x):
	return utils._cont_exp(x)

def get_emails(x):
	return utils._get_emails(x)

def remove_emails(x):
	return utils._remove_emails(x)

def get_urls(x):
	return utils._get_urls(x)

def remove_urls(x):
	return utils._remove_urls(x)

def remove_rt(x):
	return utils._remove_rt(x)

def remove_special_chars(x):
	return utils._remove_special_chars(x)

def remove_html_tags(x):
	return utils._remove_html_tags(x)

def remove_accented_chars(x):
	return utils._remove_accented_chars(x)

def remove_stopwords(x):
	return utils._remove_stopwords(x)

def make_base(x):
	return utils._make_base(x)

def get_value_counts(df, col):
	return utils._get_value_counts(df, col)

def remove_common_words(x, comm_word, n=20):
	return utils._remove_common_words(x, comm_word, n)

def remove_rare_words(x, comm_word, n=20):
	return utils._remove_rare_words(x, comm_word, n)

def spell_correction(x):
	return utils._spell_correction(x)