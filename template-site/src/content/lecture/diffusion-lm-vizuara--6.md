---
course_slug: diffusion-lm-vizuara
idx: 6
title: 'Lecture 5: Motivation behind Language Diffusion Models'
video_url: https://www.youtube.com/watch?v=3awVF05VUuM
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.3890000000000002
  end_sec: 50.0
  text: 'So I hope all of us are on the same page So I hope all of us are on the same
    page

    now with respect to the motivation now with respect to the motivation now with
    respect to the motivation

    behind this learning journey. behind this learning journey. behind this learning
    journey.

    It seems like a natural question that It seems like a natural question that It
    seems like a natural question that

    why can''t diffusion models only be why why can''t diffusion models only be why
    why can''t diffusion models only be why

    should they only be used for images? Is should they only be used for images? Is
    should they only be used for images? Is

    there some bias in our mind? This is there some bias in our mind? This is there
    some bias in our mind? This is

    exactly what Andre Karpati also talks exactly what Andre Karpati also talks exactly
    what Andre Karpati also talks

    about, right? He says that most of the about, right? He says that most of the
    about, right? He says that most of the

    image generation tools actually use image generation tools actually use image
    generation tools actually use

    diffusion and not auto reggression. diffusion and not auto reggression. diffusion
    and not auto reggression.

    We''ll see what auto reggression is in a We''ll see what auto reggression is in
    a We''ll see what auto reggression is in a

    moment. Don''t worry about it. It''s only moment. Don''t worry about it. It''s
    only moment. Don''t worry about it. It''s only

    text which has been left behind. So it text which has been left behind. So it
    text which has been left behind. So it

    is a bit of a mystery to me and many is a bit of a mystery to me and many is a
    bit of a mystery to me and many

    others that why for some reason text others that why for some reason text others
    that why for some reason text

    prefers autogeneration but image videos prefers autogeneration but image videos
    prefers autogeneration but image videos

    prefer diffusion. Why should this be? prefer diffusion. Why should this be? prefer
    diffusion. Why should this be?

    These are the kind of counterintuitive These are the kind of counterintuitive
    These are the kind of counterintuitive

    questions which researchers should ask questions which researchers should ask'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 1
  start_sec: 50.0
  end_sec: 109.04
  text: 'questions which researchers should ask

    that leads to the best research. that leads to the best research. that leads to
    the best research.

    If you ask this question, you''ll slowly If you ask this question, you''ll slowly
    If you ask this question, you''ll slowly

    start get going into a rabbit hole. You start get going into a rabbit hole. You
    start get going into a rabbit hole. You

    may end up with a new research problem may end up with a new research problem
    may end up with a new research problem

    and an impact on discovery. But the main and an impact on discovery. But the main
    and an impact on discovery. But the main

    counterintuitive question which we want counterintuitive question which we want
    counterintuitive question which we want

    to ask is why should only text prefer to ask is why should only text prefer to
    ask is why should only text prefer

    auto reggression. Right? And for images, auto reggression. Right? And for images,
    auto reggression. Right? And for images,

    videos we use diffusion. Why? videos we use diffusion. Why? videos we use diffusion.
    Why?

    A stream of papers came out which tried A stream of papers came out which tried
    A stream of papers came out which tried

    to answer this. So you''ll see that from to answer this. So you''ll see that from
    to answer this. So you''ll see that from

    2023 2022 onwards itself we have papers 2023 2022 onwards itself we have papers
    2023 2022 onwards itself we have papers

    which talk about structured denoising which talk about structured denoising which
    talk about structured denoising

    diffusion models in discrete spaces then diffusion models in discrete spaces then
    diffusion models in discrete spaces then

    discrete diffusion modeling by discrete diffusion modeling by discrete diffusion
    modeling by

    estimating the ratios of data estimating the ratios of data estimating the ratios
    of data

    distribution then simplified and distribution then simplified and distribution
    then simplified and

    generalized mask diffusion. So the generalized mask diffusion. So the generalized
    mask diffusion. So the

    concept of mask diffusion was one of the concept of mask diffusion was one of
    the concept of mask diffusion was one of the

    major breakthroughs in language modeling major breakthroughs in language modeling
    major breakthroughs in language modeling

    diffusion diffusion diffusion

    models. This so this paper I believe models. This so this paper I believe'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 2
  start_sec: 109.04
  end_sec: 171.28
  text: 'models. This so this paper I believe

    is a very important one mask diffusion is a very important one mask diffusion
    is a very important one mask diffusion

    language models this is where many language models this is where many language
    models this is where many

    things actually started to become big things actually started to become big things
    actually started to become big

    for small language diffusion models for small language diffusion models for small
    language diffusion models

    you''ll see that the paper mostly came you''ll see that the paper mostly came
    you''ll see that the paper mostly came

    from Cornell University and uh they from Cornell University and uh they from Cornell
    University and uh they

    actually actually actually

    motivated the concept of motivated the concept of motivated the concept of

    why can''t we bridge the gap between the why can''t we bridge the gap between
    the why can''t we bridge the gap between the

    diffusion models and auto reggressive diffusion models and auto reggressive diffusion
    models and auto reggressive

    methods in language modeling This was in November 2024. The most This was in November
    2024. The most

    recent paper which I am aware of which recent paper which I am aware of which
    recent paper which I am aware of which

    kind of summarizes everything and its kind of summarizes everything and its kind
    of summarizes everything and its

    state-of-the-art at this moment while state-of-the-art at this moment while state-of-the-art
    at this moment while

    recording this video or this journey recording this video or this journey recording
    this video or this journey

    videos is large language diffusion videos is large language diffusion videos is
    large language diffusion

    models. This paper came out in 18th on models. This paper came out in 18th on
    models. This paper came out in 18th on

    18th October 2025 and we are going to 18th October 2025 and we are going to 18th
    October 2025 and we are going to

    replicate this paper fully from scratch replicate this paper fully from scratch
    replicate this paper fully from scratch

    in this journey. Right. So this is a in this journey. Right. So this is a in this
    journey. Right. So this is a

    paper which paper which paper which

    actually introduces in their uh actually introduces in their uh actually introduces
    in their uh

    introduction section itself introduction section itself'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 3
  start_sec: 171.28
  end_sec: 219.84
  text: 'introduction section itself

    uh that why should images and video uh that why should images and video uh that
    why should images and video

    generation models have all the fun why generation models have all the fun why
    generation models have all the fun why

    can''t languages be used for diffusion can''t languages be used for diffusion
    can''t languages be used for diffusion

    and they actually uh talk about one more and they actually uh talk about one more
    and they actually uh talk about one more

    thing right what they talk about is that thing right what they talk about is that
    thing right what they talk about is that

    if we take a look at the probabilistic if we take a look at the probabilistic
    if we take a look at the probabilistic

    lens of looking at generative AI which lens of looking at generative AI which
    lens of looking at generative AI which

    we saw in one of the prior videos, we saw in one of the prior videos, we saw in
    one of the prior videos,

    right? If we take a look at this right? If we take a look at this right? If we
    take a look at this

    probabilistic lens, what does this lens probabilistic lens, what does this lens
    probabilistic lens, what does this lens

    say? This lens says that say? This lens says that say? This lens says that

    what is generative AI? Essentially, if what is generative AI? Essentially, if
    what is generative AI? Essentially, if

    we want to generate something, right? we want to generate something, right? we
    want to generate something, right?

    And one way to look at generation is And one way to look at generation is And
    one way to look at generation is

    finding the underlying probability finding the underlying probability finding
    the underlying probability

    distribution and sampling from it, distribution and sampling from it, distribution
    and sampling from it,

    right? What does it mean generating an right? What does it mean generating an
    right? What does it mean generating an

    image? It means finding the underlying image? It means finding the underlying
    image? It means finding the underlying

    probability distribution of where the probability distribution of where the probability
    distribution of where the

    images might lie and then sampling from images might lie and then sampling from'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 4
  start_sec: 219.84
  end_sec: 298.08
  text: 'images might lie and then sampling from

    it. So why can''t this same thing be it. So why can''t this same thing be it.
    So why can''t this same thing be

    applied to text as well? applied to text as well? applied to text as well?

    So for that let us consider that what So for that let us consider that what So
    for that let us consider that what

    does it mean to have a probability does it mean to have a probability does it
    mean to have a probability

    distribution of text distribution of text distribution of text

    and again let''s use Google Gemini and again let''s use Google Gemini and again
    let''s use Google Gemini

    because as I told you I want you to show because as I told you I want you to show
    because as I told you I want you to show

    I want to show you how I learned. So I want to show you how I learned. So I want
    to show you how I learned. So

    I''ll ask here that I understood I''ll ask here that I understood I''ll ask here
    that I understood

    the concept of probability distribution for images and how images distribution
    for images and how images

    might live in high dimensional might live in high dimensional might live in high
    dimensional

    pixel spaces. pixel spaces. pixel spaces.

    What about text? How can they live in high dimensional How can they live in high
    dimensional

    spaces? spaces? spaces?

    What does it mean? Probability Probability

    distribution of meaningful text. So I distribution of meaningful text. So I distribution
    of meaningful text. So I

    want all of you to pause here and think want all of you to pause here and think
    want all of you to pause here and think

    about this for a moment. If I ask you about this for a moment. If I ask you about
    this for a moment. If I ask you

    this question in an interview, how would this question in an interview, how would
    this question in an interview, how would

    you answer this? you answer this? you answer this?

    Well, the way I would think about it is Well, the way I would think about it is
    Well, the way I would think about it is

    when we talked about images, first we when we talked about images, first we'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 5
  start_sec: 298.08
  end_sec: 354.95
  text: 'when we talked about images, first we

    broke down the images into pixels, broke down the images into pixels, broke down
    the images into pixels,

    right? Similarly, text can be broken right? Similarly, text can be broken right?
    Similarly, text can be broken

    down into tokens, broken down into token down into tokens, broken down into token
    down into tokens, broken down into token

    ids and they can also be represented in ids and they can also be represented in
    ids and they can also be represented in

    higher dimensional pixel spaces. In this higher dimensional pixel spaces. In this
    higher dimensional pixel spaces. In this

    they can be represented in high they can be represented in high they can be represented
    in high

    dimensional token space. In this huge dimensional token space. In this huge dimensional
    token space. In this huge

    highdimensional token space, there might highdimensional token space, there might
    highdimensional token space, there might

    be only a very small area which consists be only a very small area which consists
    be only a very small area which consists

    of meaningful text. So let''s say this is of meaningful text. So let''s say this
    is of meaningful text. So let''s say this is

    a higher dimensional token space of a higher dimensional token space of a higher
    dimensional token space of

    sentences. All possible sentences in sentences. All possible sentences in sentences.
    All possible sentences in

    human history. There might be only a human history. There might be only a human
    history. There might be only a

    small area of meaningful text and this small area of meaningful text and this
    small area of meaningful text and this

    might have certain probability might have certain probability might have certain
    probability

    distribution. This is what generating distribution. This is what generating distribution.
    This is what generating

    meaningful sentences might mean. So one meaningful sentences might mean. So one
    meaningful sentences might mean. So one

    way of looking at generating sentences way of looking at generating sentences
    way of looking at generating sentences

    is just this, right? create generate is just this, right? create generate is just
    this, right? create generate

    create a poem on let''s say create a poem on let''s say create a poem on let''s
    say

    uh diffusion models. uh diffusion models. uh diffusion models.

    So one way to look at generating text is'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 6
  start_sec: 354.95
  end_sec: 417.52
  text: 'So one way to look at generating text is So one way to look at generating
    text is

    just one word at a time. Another way of just one word at a time. Another way of
    just one word at a time. Another way of

    looking at generating text is finding looking at generating text is finding looking
    at generating text is finding

    this probability distribution where this probability distribution where this probability
    distribution where

    meaningful text lives related to my meaningful text lives related to my meaningful
    text lives related to my

    given sentence. So conditional given sentence. So conditional given sentence.
    So conditional

    probability distribution related to my probability distribution related to my
    probability distribution related to my

    input prompt and then sampling from it. input prompt and then sampling from it.
    input prompt and then sampling from it.

    This part which I''m speaking is the key This part which I''m speaking is the
    key This part which I''m speaking is the key

    intuition behind language diffusion intuition behind language diffusion intuition
    behind language diffusion

    models. models. models.

    One another way of looking at generating One another way of looking at generating
    One another way of looking at generating

    text is finding this probability text is finding this probability text is finding
    this probability

    distribution where meaningful text lives distribution where meaningful text lives
    distribution where meaningful text lives

    conditioned to the input prompt and then conditioned to the input prompt and then
    conditioned to the input prompt and then

    sampling from it. So yeah, maybe this poem is sampled from So yeah, maybe this
    poem is sampled from

    the meaningful space where the text the meaningful space where the text the meaningful
    space where the text

    actually lives. Let''s see. So this would be my answer if Let''s see. So this
    would be my answer if

    this was asked in an interview. Let''s this was asked in an interview. Let''s
    this was asked in an interview. Let''s

    see what Google Gemini has to say about see what Google Gemini has to say about
    see what Google Gemini has to say about

    this. What about text? How can they live this. What about text? How can they live
    this. What about text? How can they live

    in high dimensional spaces? What does it in high dimensional spaces? What does
    it'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 7
  start_sec: 417.52
  end_sec: 492.629
  text: 'in high dimensional spaces? What does it

    mean probability distribution of mean probability distribution of mean probability
    distribution of

    meaningful text? Let''s see. So text is trickier than images. So text is trickier
    than images.

    With images you had 128x 128 pixels. In With images you had 128x 128 pixels. In
    With images you had 128x 128 pixels. In

    text words can be converted into text words can be converted into text words can
    be converted into

    embeddings. That''s even awesome, right? embeddings. That''s even awesome, right?
    embeddings. That''s even awesome, right?

    Words can be converted into higher Words can be converted into higher Words can
    be converted into higher

    dimensional vector spaces. uh and each dimensional vector spaces. uh and each
    dimensional vector spaces. uh and each

    embedding vector can be in a higher embedding vector can be in a higher embedding
    vector can be in a higher

    dimensional space. Awesome. dimensional space. Awesome. dimensional space. Awesome.

    To understand the probability To understand the probability To understand the
    probability

    distribution, imagine a book space. So distribution, imagine a book space. So
    distribution, imagine a book space. So

    suppose we define a book as any sequence suppose we define a book as any sequence
    suppose we define a book as any sequence

    of 100,000 characters. This is a huge of 100,000 characters. This is a huge of
    100,000 characters. This is a huge

    number of characters and a huge >> okay I found this on the web. So this is >>
    okay I found this on the web. So this is

    >> Siri got activated for some reason. The >> Siri got activated for some reason.
    The >> Siri got activated for some reason. The

    what it means to generate meaningful what it means to generate meaningful what
    it means to generate meaningful

    text is in this huge space to find that text is in this huge space to find that
    text is in this huge space to find that

    set of characters which are meaningful. Uh Uh

    if you feed the sentence, so the if you feed the sentence, so the if you feed
    the sentence, so the

    probability distribution is a probability distribution is a probability distribution
    is a

    mathematical function that scores a mathematical function that scores a mathematical
    function that scores a

    sequence of words based on two things.'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 8
  start_sec: 492.629
  end_sec: 552.71
  text: 'sequence of words based on two things. sequence of words based on two things.

    Grammar and logic both need to be Grammar and logic both need to be Grammar and
    logic both need to be

    correct, right? And that probably lives correct, right? And that probably lives
    correct, right? And that probably lives

    in a small space in this higher in a small space in this higher in a small space
    in this higher

    dimensional area. That''s the way to think about That''s the way to think about

    probability distribution for text, probability distribution for text, probability
    distribution for text,

    right? So why can''t we find this right? So why can''t we find this right? So
    why can''t we find this

    probability distribution where the probability distribution where the probability
    distribution where the

    meaningful text lies using diffusion? If meaningful text lies using diffusion?
    If meaningful text lies using diffusion? If

    this if generative AI can be looked at this if generative AI can be looked at
    this if generative AI can be looked at

    through a probabilistic lens, why should through a probabilistic lens, why should
    through a probabilistic lens, why should

    it be restricted to images? Why not it be restricted to images? Why not it be
    restricted to images? Why not

    text? That''s what this these people text? That''s what this these people text?
    That''s what this these people

    actually asked, actually asked, actually asked,

    right? What they said is that if you look at how language models if you look at
    how language models

    traditionally operate, it''s through the traditionally operate, it''s through
    the traditionally operate, it''s through the

    concept of auto reggression which we are concept of auto reggression which we
    are concept of auto reggression which we are

    going to look at very soon. But what going to look at very soon. But what going
    to look at very soon. But what

    these people proposed is that the major these people proposed is that the major
    these people proposed is that the major

    reason why reason why reason why

    uh uh uh

    major reason why diffusion models work major reason why diffusion models work
    major reason why diffusion models work

    for images can be the same reason which for images can be the same reason which
    for images can be the same reason which

    can be carried forward to languages.'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
- idx: 9
  start_sec: 552.71
  end_sec: 571.68
  text: 'can be carried forward to languages. can be carried forward to languages.

    What these people suggested is auto What these people suggested is auto What these
    people suggested is auto

    reggressive models or auto reggressive reggressive models or auto reggressive
    reggressive models or auto reggressive

    methods are not the reason for LLMs to methods are not the reason for LLMs to
    methods are not the reason for LLMs to

    work. So why are we sticking to it? work. So why are we sticking to it? work.
    So why are we sticking to it?

    Let''s look at auto reggression actually Let''s look at auto reggression actually
    Let''s look at auto reggression actually

    right now so that all of you have some right now so that all of you have some
    right now so that all of you have some

    baseline to compare to.'
  concept_slugs:
  - autoregressive-vs-diffusion
  - diffusion-language-model
---
# Lecture 5: Motivation behind Language Diffusion Models

See the structured chunks above.
