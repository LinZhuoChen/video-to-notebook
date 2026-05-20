---
course_slug: cmu-10799-diffusion-flow
idx: 11
title: 'CMU 10799 S26: Lecture 12 - Discrete Diffusion & Masked Diffusion - Diffusion
  & Flow Matching'
video_url: https://www.youtube.com/watch?v=mXEjZblUBPs
duration_sec: null
chunks:
- idx: 0
  start_sec: 2.55
  end_sec: 56.31
  text: 'All right. All right.

    Right. So, so far what we have learn we Right. So, so far what we have learn we
    Right. So, so far what we have learn we

    have learned about like pretty much have learned about like pretty much have learned
    about like pretty much

    everything about diffusion models or everything about diffusion models or everything
    about diffusion models or

    like the overall family of the diffusion like the overall family of the diffusion
    like the overall family of the diffusion

    models right for image generation models right for image generation models right
    for image generation

    specifically. Uh so we have covered the specifically. Uh so we have covered the
    specifically. Uh so we have covered the

    fundamentals the denoising the diffusion fundamentals the denoising the diffusion
    fundamentals the denoising the diffusion

    models the scorebased models and models the scorebased models and models the scorebased
    models and

    the full matching all of them are pretty the full matching all of them are pretty
    the full matching all of them are pretty

    much the same thing right and in order much the same thing right and in order
    much the same thing right and in order

    to improve upon that we have covered a to improve upon that we have covered a
    to improve upon that we have covered a

    bunch of advanced topics that includes bunch of advanced topics that includes
    bunch of advanced topics that includes

    the design space of diffusion model uh the design space of diffusion model uh
    the design space of diffusion model uh

    you know how can we do faster sampling you know how can we do faster sampling
    you know how can we do faster sampling

    by various inference time method uh how by various inference time method uh how
    by various inference time method uh how

    can we do controllable generations and can we do controllable generations and
    can we do controllable generations and

    specifically how can we do test the specifically how can we do test the specifically
    how can we do test the

    image generation and we last week we image generation and we last week we image
    generation and we last week we

    also talked about many different you also talked about many different you also
    talked about many different you

    know method know method know method

    to do distillation or uh you know self'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 1
  start_sec: 56.31
  end_sec: 105.119
  text: 'to do distillation or uh you know self to do distillation or uh you know
    self

    dissolations or flow maps or consistency dissolations or flow maps or consistency
    dissolations or flow maps or consistency

    models those things um but on the other models those things um but on the other
    models those things um but on the other

    hand I know a lot of you guys are from hand I know a lot of you guys are from
    hand I know a lot of you guys are from

    LTI LTI LTI

    so far everything we have learned about so far everything we have learned about
    so far everything we have learned about

    are about image or uh in image that''s are about image or uh in image that''s
    are about image or uh in image that''s

    get represented in a continuous space get represented in a continuous space get
    represented in a continuous space

    right because you know in your homework right because you know in your homework
    right because you know in your homework

    one and two you need to like you know one and two you need to like you know one
    and two you need to like you know

    rescale it to negative one and one and rescale it to negative one and one and
    rescale it to negative one and one and

    stuff, right? So the the problem stuff, right? So the the problem stuff, right?
    So the the problem

    is that then how about discrete data is that then how about discrete data is that
    then how about discrete data

    then? Like then? Like then? Like

    is it possible for us to extend what we is it possible for us to extend what we
    is it possible for us to extend what we

    have learned to discrete data? Now why have learned to discrete data? Now why
    have learned to discrete data? Now why

    do we care about discrete data is do we care about discrete data is do we care
    about discrete data is

    because it''s actually quite important. because it''s actually quite important.
    because it''s actually quite important.

    Matter of fact, some people, not to name Matter of fact, some people, not to name
    Matter of fact, some people, not to name

    who, actually, I''ll just name who, like who, actually, I''ll just name who, like'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 2
  start_sec: 105.119
  end_sec: 157.519
  text: 'who, actually, I''ll just name who, like

    the people from Anthropic have claimed the people from Anthropic have claimed
    the people from Anthropic have claimed

    to me that uh I I believe it''s ICML 2024 to me that uh I I believe it''s ICML
    2024 to me that uh I I believe it''s ICML 2024

    that like uh they said, well, anything that like uh they said, well, anything
    that like uh they said, well, anything

    that cannot be expressed or compressed that cannot be expressed or compressed
    that cannot be expressed or compressed

    into text is uninteresting information into text is uninteresting information
    into text is uninteresting information

    and uh you know, image generation is and uh you know, image generation is and
    uh you know, image generation is

    just not on the path to AGI. This is just not on the path to AGI. This is just
    not on the path to AGI. This is

    what they said. Okay, rumor has that what they said. Okay, rumor has that what
    they said. Okay, rumor has that

    they''re going to release a image uh they''re going to release a image uh they''re
    going to release a image uh

    generation model. So, we shall see if generation model. So, we shall see if generation
    model. So, we shall see if

    it''s actually on the path to AGI. But it''s actually on the path to AGI. But
    it''s actually on the path to AGI. But

    regardless, you know, all of those AGI regardless, you know, all of those AGI
    regardless, you know, all of those AGI

    bros probably uh they really believe bros probably uh they really believe bros
    probably uh they really believe

    that text is like uh like the the path that text is like uh like the the path
    that text is like uh like the the path

    to, you know, super intelligence and to, you know, super intelligence and to,
    you know, super intelligence and

    whatever. So, it''s like super important whatever. So, it''s like super important
    whatever. So, it''s like super important

    I guess right now uh for investment I guess right now uh for investment I guess
    right now uh for investment

    reasons and whatever. Um reasons and whatever. Um reasons and whatever. Um

    uh I mean obviously you know we have uh I mean obviously you know we have'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 3
  start_sec: 157.519
  end_sec: 215.599
  text: 'uh I mean obviously you know we have

    other important modalities right for other important modalities right for other
    important modalities right for

    example like molecules or like DNA example like molecules or like DNA example
    like molecules or like DNA

    sequences and stuff right and those sequences and stuff right and those sequences
    and stuff right and those

    things are oftent times at least things are oftent times at least things are oftent
    times at least

    partially um represented by uh discrete partially um represented by uh discrete
    partially um represented by uh discrete

    data and moreover even image right so data and moreover even image right so data
    and moreover even image right so

    like right now like right now like right now

    do we store image is by not actually in do we store image is by not actually in
    do we store image is by not actually in

    a continuous space but actually in like a continuous space but actually in like
    a continuous space but actually in like

    a quantiz a quantiz a quantiz

    discretized pixel space, right? So you discretized pixel space, right? So you
    discretized pixel space, right? So you

    actually what you''re seeing is a bunch actually what you''re seeing is a bunch
    actually what you''re seeing is a bunch

    of like different pixels and each pixel of like different pixels and each pixel
    of like different pixels and each pixel

    actually has three channels and each actually has three channels and each actually
    has three channels and each

    channel actually has a value like a channel actually has a value like a channel
    actually has a value like a

    discrete value from 0 to 255, right? So discrete value from 0 to 255, right? So
    discrete value from 0 to 255, right? So

    this is like technically image should this is like technically image should this
    is like technically image should

    also be represented as discrete data. So also be represented as discrete data.
    So also be represented as discrete data. So

    uh uh uh

    how do we make diffusion models work on how do we make diffusion models work on
    how do we make diffusion models work on

    discrete data? discrete data? discrete data?

    What? Yes. What? Yes. What? Yes.

    >> Near space and do like a nearest >> Near space and do like a nearest'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 4
  start_sec: 215.599
  end_sec: 284.24
  text: '>> Near space and do like a nearest

    neighbors type thing to match it. neighbors type thing to match it. neighbors
    type thing to match it.

    >> Uh so diffusion model on a continuous >> Uh so diffusion model on a continuous
    >> Uh so diffusion model on a continuous

    space and then do nearest neighbor. This space and then do nearest neighbor. This
    space and then do nearest neighbor. This

    is a good good uh good uh good approach. is a good good uh good uh good approach.
    is a good good uh good uh good approach.

    Uh are do you have any allergies? Great. Uh are do you have any allergies? Great.
    Uh are do you have any allergies? Great.

    All right. All right.

    It has nuts in it. So that''s why I need It has nuts in it. So that''s why I need
    It has nuts in it. So that''s why I need

    to ask. All right. Uh, do you prefer to to ask. All right. Uh, do you prefer to
    to ask. All right. Uh, do you prefer to

    have blessing on getting rich or getting have blessing on getting rich or getting
    have blessing on getting rich or getting

    good academic achievement? good academic achievement? good academic achievement?

    >> I think they''re related. >> I think they''re related. >> I think they''re
    related.

    >> Well, which one you choose one? >> Well, which one you choose one? >> Well,
    which one you choose one?

    >> Maybe rich. The other one I can do. >> Maybe rich. The other one I can do.
    >> Maybe rich. The other one I can do.

    >> Okay. >> Okay. >> Okay.

    All right. All right.

    All right. Anyone else want to have a All right. Anyone else want to have a All
    right. Anyone else want to have a

    take a guess take a guess take a guess

    or like some you know attempt I hear something but I don''t see okay I hear something
    but I don''t see okay

    so even right now text is first gone it so even right now text is first gone it
    so even right now text is first gone it

    goes through an embedding process and goes through an embedding process and goes
    through an embedding process and

    then embedding is what goes through then embedding is what goes through'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 5
  start_sec: 284.24
  end_sec: 326.72
  text: 'then embedding is what goes through

    >> so you first take the text and go to >> so you first take the text and go to
    >> so you first take the text and go to

    embedding embedding existing embedding embedding existing embedding embedding
    existing

    of the embeddings of the embeddings of the embeddings

    >> and then when you have to unimpify it >> and then when you have to unimpify
    it >> and then when you have to unimpify it

    that time then you need some other model that time then you need some other model
    that time then you need some other model

    to do the to do the to do the

    >> decoding or something right okay so you >> decoding or something right okay
    so you >> decoding or something right okay so you

    guys kind of have a similar uh like idea guys kind of have a similar uh like idea
    guys kind of have a similar uh like idea

    and this idea actually was explored by and this idea actually was explored by
    and this idea actually was explored by

    people from Stanford and it''s actually people from Stanford and it''s actually
    people from Stanford and it''s actually

    also it''s like kind of like the first also it''s like kind of like the first
    also it''s like kind of like the first

    like diffusion language model if you like diffusion language model if you like
    diffusion language model if you

    will uh but this is like pretty much will uh but this is like pretty much will
    uh but this is like pretty much

    exactly what they did uh unfortunately exactly what they did uh unfortunately
    exactly what they did uh unfortunately

    it it didn''t work as well as what we''re it it didn''t work as well as what we''re
    it it didn''t work as well as what we''re

    going to talk about today. But that was going to talk about today. But that was
    going to talk about today. But that was

    the first attempt. Do I have allergies? the first attempt. Do I have allergies?
    the first attempt. Do I have allergies?

    All right. Get get uh I''m kind of All right. Get get uh I''m kind of All right.
    Get get uh I''m kind of

    running out of the allergyfree options. running out of the allergyfree options.'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 6
  start_sec: 326.72
  end_sec: 379.11
  text: 'running out of the allergyfree options.

    Hold on. Uh sorry. The the allergy Hold on. Uh sorry. The the allergy Hold on.
    Uh sorry. The the allergy

    sensitive option. Okay. Anyway, you''re sensitive option. Okay. Anyway, you''re
    sensitive option. Okay. Anyway, you''re

    getting something that is an allergy getting something that is an allergy getting
    something that is an allergy

    invariant. Uh invariant. Uh invariant. Uh

    uh uh uh. Do you want to get rich or do uh uh uh. Do you want to get rich or do
    uh uh uh. Do you want to get rich or do

    you want to get you want to get you want to get

    >> Okay. Dang. I don''t want to get rich. That''s Dang. I don''t want to get rich.
    That''s

    crazy. All right. Anyway, crazy. All right. Anyway, crazy. All right. Anyway,

    okay. Um anyway, but um if you if we okay. Um anyway, but um if you if we okay.
    Um anyway, but um if you if we

    think about it, right, diffusion models think about it, right, diffusion models
    think about it, right, diffusion models

    can be viewed in three ways, right? As can be viewed in three ways, right? As
    can be viewed in three ways, right? As

    we have mentioned before, at least we have mentioned before, at least we have
    mentioned before, at least

    continuous diffusion. We have denoising continuous diffusion. We have denoising
    continuous diffusion. We have denoising

    diffusion models, which is basically diffusion models, which is basically diffusion
    models, which is basically

    we''re trying to learn well add noise in we''re trying to learn well add noise
    in we''re trying to learn well add noise in

    the forward process and learn to dn the forward process and learn to dn the forward
    process and learn to dn

    noiseise in the in the reverse process. noiseise in the in the reverse process.
    noiseise in the in the reverse process.

    And in the scorebased models, we''re And in the scorebased models, we''re And
    in the scorebased models, we''re

    trying to learn a score function and trying to learn a score function and trying
    to learn a score function and

    then somehow sample through a OD or SDE. then somehow sample through a OD or SDE.
    then somehow sample through a OD or SDE.

    And then uh for flow matching is pretty'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 7
  start_sec: 379.11
  end_sec: 423.68
  text: 'And then uh for flow matching is pretty And then uh for flow matching is
    pretty

    much the same thing, but instead of much the same thing, but instead of much the
    same thing, but instead of

    learning the score function directly, learning the score function directly, learning
    the score function directly,

    we''re learning some velocity, right? So we''re learning some velocity, right?
    So we''re learning some velocity, right? So

    basically can do we have like the like a basically can do we have like the like
    a basically can do we have like the like a

    like a mapping from the formulations in like a mapping from the formulations in
    like a mapping from the formulations in

    continuous diffusion to discrete continuous diffusion to discrete continuous diffusion
    to discrete

    diffusion. This is the question that diffusion. This is the question that diffusion.
    This is the question that

    we''re mainly going to be as uh be we''re mainly going to be as uh be we''re mainly
    going to be as uh be

    answering today. Okay, so let''s look at answering today. Okay, so let''s look
    at answering today. Okay, so let''s look at

    the first or maybe the most like naive the first or maybe the most like naive
    the first or maybe the most like naive

    way to think about this, right? Um, so way to think about this, right? Um, so
    way to think about this, right? Um, so

    say like how do we add noise uh and say like how do we add noise uh and say like
    how do we add noise uh and

    learn to d noiseise in a discrete space learn to d noiseise in a discrete space
    learn to d noiseise in a discrete space

    first. Okay, so let''s get a reminder of first. Okay, so let''s get a reminder
    of first. Okay, so let''s get a reminder of

    how diffusion works. I''m sure you guys how diffusion works. I''m sure you guys
    how diffusion works. I''m sure you guys

    know, but like you know you just add know, but like you know you just add know,
    but like you know you just add

    noise and then gradually d noiseise. The noise and then gradually d noiseise.
    The noise and then gradually d noiseise. The

    adding noise process is the forward adding noise process is the forward'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 8
  start_sec: 423.68
  end_sec: 489.039
  text: 'adding noise process is the forward

    process and the gradually d noiseis process and the gradually d noiseis process
    and the gradually d noiseis

    process is the reverse process. Right. process is the reverse process. Right.
    process is the reverse process. Right.

    So I guess the first question is how do So I guess the first question is how do
    So I guess the first question is how do

    we define noise quote unquote in say we define noise quote unquote in say we define
    noise quote unquote in say

    like a text space right? Okay like a text space right? Okay like a text space
    right? Okay

    >> tokens. >> tokens. >> tokens.

    >> Masking tokens. Okay. Good idea. Anyone >> Masking tokens. Okay. Good idea.
    Anyone >> Masking tokens. Okay. Good idea. Anyone

    else? Yeah. >> Incorrect like just like rand random >> Incorrect like just like
    rand random

    things, right? Basically things, right? Basically things, right? Basically

    >> Yeah. Yeah. Yeah. like wrong tokens. >> Yeah. Yeah. Yeah. like wrong tokens.
    >> Yeah. Yeah. Yeah. like wrong tokens.

    Okay, great. Uh well, allergy. Okay, great. Uh well, allergy. Okay, great. Uh
    well, allergy.

    Okay, everything is a vegetarian by the Okay, everything is a vegetarian by the
    Okay, everything is a vegetarian by the

    way, so no worries. But let''s hope Oh. way, so no worries. But let''s hope Oh.
    way, so no worries. But let''s hope Oh.

    Uh okay. Uh good academic or ah man, you Uh okay. Uh good academic or ah man,
    you Uh okay. Uh good academic or ah man, you

    guys are just uh too serious. Okay. guys are just uh too serious. Okay. guys are
    just uh too serious. Okay.

    Okay. Or okay. All right. Okay. Or okay. All right. Okay. Or okay. All right.

    Cool. Anyway. Cool. Anyway. Cool. Anyway.

    All right. So let''s see All right. So let''s see All right. So let''s see

    the like how do we define noise in text the like how do we define noise in text
    the like how do we define noise in text

    right so let''s this is like a noised right so let''s this is like a noised right
    so let''s this is like a noised

    version of a tweet from Andre Kapathi uh version of a tweet from Andre Kapathi
    uh'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 9
  start_sec: 489.039
  end_sec: 555.509
  text: 'version of a tweet from Andre Kapathi uh

    so let''s identify some of the noise in so let''s identify some of the noise in
    so let''s identify some of the noise in

    this tweet what do we see this tweet what do we see this tweet what do we see

    >> I see random emojis in between and >> I see random emojis in between and >>
    I see random emojis in between and

    random characters random characters random characters

    >> random emojis >> random emojis >> random emojis

    all right you''re getting allergy all right you''re getting allergy all right
    you''re getting allergy

    >> all right hold on >> all right hold on >> all right hold on

    poor Dvanchu is getting uh invarian poor Dvanchu is getting uh invarian poor Dvanchu
    is getting uh invarian

    version but it''s okay. All right. Uh version but it''s okay. All right. Uh version
    but it''s okay. All right. Uh

    academic or >> get rich. >> get rich.

    Okay. All right. Okay. All right. Okay. All right.

    Okay. Uh random emojis. What else? Okay. Uh random emojis. What else? Okay. Uh
    random emojis. What else?

    >> Spellings are wrong. >> Spellings are wrong. >> Spellings are wrong.

    >> Spellings are wrong. >> Spellings are wrong.

    Hold on. Hold on. Hold on. Hold on. Hold on. Hold on.

    Get rich or Get rich or Get rich or

    >> Okay. >> Okay.

    Oh, this is actually a good one. way the Oh, this is actually a good one. way
    the Oh, this is actually a good one. way the

    the the envelope. Okay. Uh the the envelope. Okay. Uh the the envelope. Okay.
    Uh

    uh yeah, but basically pretty much that, uh yeah, but basically pretty much that,
    uh yeah, but basically pretty much that,

    right? So like so this is the original right? So like so this is the original
    right? So like so this is the original

    tweet and you''ll get like some random tweet and you''ll get like some random
    tweet and you''ll get like some random

    tokens here and there. You get some like tokens here and there. You get some like
    tokens here and there. You get some like

    weird modifications to the tokens and weird modifications to the tokens and weird
    modifications to the tokens and

    then you get some weird emojis and you'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 10
  start_sec: 555.509
  end_sec: 613.44
  text: 'then you get some weird emojis and you then you get some weird emojis and
    you

    get some like out of place like six, get some like out of place like six, get
    some like out of place like six,

    seven like tokens just who knows what''s seven like tokens just who knows what''s
    seven like tokens just who knows what''s

    going on. Um yeah so essentially these going on. Um yeah so essentially these
    going on. Um yeah so essentially these

    are the noise right then uh how so if we are the noise right then uh how so if
    we are the noise right then uh how so if we

    want to define noise as something like want to define noise as something like
    want to define noise as something like

    that basically just some random out that basically just some random out that basically
    just some random out

    ofplace tokens then how do we add noise ofplace tokens then how do we add noise
    ofplace tokens then how do we add noise

    then to the text then to the text then to the text

    to a piece of like given a piece of text to a piece of like given a piece of text
    to a piece of like given a piece of text

    how do we add noise how do we add noise how do we add noise

    >> well yeah >> well yeah >> well yeah

    that is uh well hold on who who who that is uh well hold on who who who that is
    uh well hold on who who who

    raised their hands first I actually raised their hands first I actually raised
    their hands first I actually

    don''t okay yeah don''t okay yeah don''t okay yeah

    >> I don''t know something irrelevant. >> I don''t know something irrelevant.
    >> I don''t know something irrelevant.

    >> Add something add something irrelevant. >> Add something add something irrelevant.
    >> Add something add something irrelevant.

    Sort sort of sort of but um uh maybe Sort sort of sort of but um uh maybe Sort
    sort of sort of but um uh maybe

    formalize it as like a say given a piece formalize it as like a say given a piece
    formalize it as like a say given a piece

    of text. >> Yeah. Okay.'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 11
  start_sec: 613.44
  end_sec: 683.04
  text: '>> Yeah. Okay.

    >> Masking also works. Okay. Uh hold on. Uh >> Masking also works. Okay. Uh hold
    on. Uh >> Masking also works. Okay. Uh hold on. Uh

    do you have allergy? Okay. This is also do you have allergy? Okay. This is also
    do you have allergy? Okay. This is also

    allergy inv. Do you have allergy inv. Do you have allergy inv. Do you have

    >> get rich or >> get rich or >> get rich or

    >> both? >> both? >> both?

    >> Choose. >> Choose. >> Choose.

    >> Oh, yeah. Ask him too much, man. Only >> Oh, yeah. Ask him too much, man. Only
    >> Oh, yeah. Ask him too much, man. Only

    one. Okay. You''re getting rich. Okay. one. Okay. You''re getting rich. Okay.
    one. Okay. You''re getting rich. Okay.

    What about you? What about you? What about you?

    >> Hold on. Hold on. No allergy. >> Hold on. Hold on. No allergy. >> Hold on.
    Hold on. No allergy.

    Give me a sec. All right. Let''s see. Let''s see.

    Uh, no. Okay. Uh, no. Okay. Uh, no. Okay.

    This is the allergen version, I guess. This is the allergen version, I guess.
    This is the allergen version, I guess.

    Dang, nobody has allergy in this class. Dang, nobody has allergy in this class.
    Dang, nobody has allergy in this class.

    This is amazing. This is amazing. This is amazing.

    >> Okay. Uh, which one? Get rich. >> Okay. Uh, which one? Get rich. >> Okay. Uh,
    which one? Get rich.

    >> Rich for sure. >> Rich for sure. >> Rich for sure.

    >> Okay. Oh, thank you. Um anyway, >> Okay. Oh, thank you. Um anyway, >> Okay.
    Oh, thank you. Um anyway,

    yeah, but essentially yeah, but essentially yeah, but essentially

    the idea is that the idea is that the idea is that

    the idea is that like for every token, the idea is that like for every token,
    the idea is that like for every token,

    we can just have some like random we can just have some like random we can just
    have some like random

    probability that transform this token probability that transform this token probability
    that transform this token

    from the like original uh clean data to from the like original uh clean data to'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 12
  start_sec: 683.04
  end_sec: 743.75
  text: 'from the like original uh clean data to

    some random tokens right in the some random tokens right in the some random tokens
    right in the

    vocabulary. So that basically say like vocabulary. So that basically say like
    vocabulary. So that basically say like

    you just randomly select a token and you just randomly select a token and you
    just randomly select a token and

    then this token get randomly transformed then this token get randomly transformed
    then this token get randomly transformed

    into 67 right okay so mathematically into 67 right okay so mathematically into
    67 right okay so mathematically

    uh or like I guess like not so formally uh or like I guess like not so formally
    uh or like I guess like not so formally

    mathematically how we say just let''s say mathematically how we say just let''s
    say mathematically how we say just let''s say

    we have a vocabulary uh say like the we have a vocabulary uh say like the we have
    a vocabulary uh say like the

    vocabulary is really short just I love vocabulary is really short just I love
    vocabulary is really short just I love

    cat three possible tokens and uh then cat three possible tokens and uh then cat
    three possible tokens and uh then

    the sentence I love cat can be the sentence I love cat can be the sentence I love
    cat can be

    represented by three one whole vectors represented by three one whole vectors
    represented by three one whole vectors

    vectors. Uh vectors. Uh vectors. Uh

    the one half vectors is incorrect the one half vectors is incorrect the one half
    vectors is incorrect

    because I you I wanted to have five because I you I wanted to have five because
    I you I wanted to have five

    tokens but then it''s too much math to tokens but then it''s too much math to
    tokens but then it''s too much math to

    do. So uh but yeah the one half vector do. So uh but yeah the one half vector
    do. So uh but yeah the one half vector

    should be give me a second. All right. Anyway you can you can All right. Anyway
    you can you can

    represent everything in a one half represent everything in a one half represent
    everything in a one half

    vector. Uh then basically say we have a'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 13
  start_sec: 743.75
  end_sec: 789.67
  text: 'vector. Uh then basically say we have a vector. Uh then basically say we
    have a

    beta chance. This is just a some chance beta chance. This is just a some chance
    beta chance. This is just a some chance

    to turn that an existing token into a to turn that an existing token into a to
    turn that an existing token into a

    random one in the vocabulary. Uh that random one in the vocabulary. Uh that random
    one in the vocabulary. Uh that

    this transformation can be represented this transformation can be represented
    this transformation can be represented

    by this transition matrix essentially uh by this transition matrix essentially
    uh by this transition matrix essentially uh

    which we represent as Q. Uh where yeah which we represent as Q. Uh where yeah
    which we represent as Q. Uh where yeah

    like it''s literally just like um sorry like it''s literally just like um sorry
    like it''s literally just like um sorry

    not beta. Yeah. So it''s literally not beta. Yeah. So it''s literally not beta.
    Yeah. So it''s literally

    because we have a beta chance to uh you because we have a beta chance to uh you
    because we have a beta chance to uh you

    know sample it to be any um like know sample it to be any um like know sample
    it to be any um like

    vocabulary in uh any token in the vocabulary in uh any token in the vocabulary
    in uh any token in the

    vocabulary. You can also resample the vocabulary. You can also resample the vocabulary.
    You can also resample the

    same one. So that''s why it''s basically same one. So that''s why it''s basically
    same one. So that''s why it''s basically

    just like every everyone has like just like every everyone has like just like
    every everyone has like

    onethird of beta of a chance to get onethird of beta of a chance to get onethird
    of beta of a chance to get

    sampled when we try to you know resample sampled when we try to you know resample
    sampled when we try to you know resample

    but otherwise we stay the same. So this but otherwise we stay the same. So this
    but otherwise we stay the same. So this

    is why this is like one minus you know'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 14
  start_sec: 789.67
  end_sec: 848.629
  text: 'is why this is like one minus you know is why this is like one minus you
    know

    every everything else has one beta over every everything else has one beta over
    every everything else has one beta over

    three chance and then staying the same three chance and then staying the same
    three chance and then staying the same

    has a 1 minus 2 beta over 3. has a 1 minus 2 beta over 3. has a 1 minus 2 beta
    over 3.

    Okay, make sense? Okay, make sense? Okay, make sense?

    All right. Now, uh let''s apply this All right. Now, uh let''s apply this All
    right. Now, uh let''s apply this

    transition matrix to the third token say transition matrix to the third token
    say transition matrix to the third token say

    cat, right? Uh then we literally just do cat, right? Uh then we literally just
    do cat, right? Uh then we literally just do

    you know one hot vector times transition you know one hot vector times transition
    you know one hot vector times transition

    matrix equals to the new uh probability matrix equals to the new uh probability
    matrix equals to the new uh probability

    like literally equal to the new like like literally equal to the new like like
    literally equal to the new like

    probability distribution. So essentially probability distribution. So essentially
    probability distribution. So essentially

    right now this is like you have like right now this is like you have like right
    now this is like you have like

    beta over three chance to get transition beta over three chance to get transition
    beta over three chance to get transition

    into I uh beta over three chance to get into I uh beta over three chance to get
    into I uh beta over three chance to get

    transition love and then one minus 2 transition love and then one minus 2 transition
    love and then one minus 2

    beta over three chance into staying at beta over three chance into staying at
    beta over three chance into staying at

    cat. Okay cat. Okay cat. Okay

    any question? Yeah, any question? Yeah, any question? Yeah,

    >> when we actually do this for real >> when we actually do this for real >> when
    we actually do this for real

    sentences with real vocabulary, it''s not'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 15
  start_sec: 848.629
  end_sec: 910.069
  text: 'sentences with real vocabulary, it''s not sentences with real vocabulary,
    it''s not

    necessary that the noise sentence is necessary that the noise sentence is necessary
    that the noise sentence is

    actually like it might like there is a actually like it might like there is a
    actually like it might like there is a

    chance that say we replace some word chance that say we replace some word chance
    that say we replace some word

    which is not conse. >> Yes, that''s right. But like just think >> Yes, that''s
    right. But like just think

    about how many like tokens available out about how many like tokens available
    out about how many like tokens available out

    there, right? the chances of that is non there, right? the chances of that is
    non there, right? the chances of that is non

    zero but like also not high right okay zero but like also not high right okay
    zero but like also not high right okay

    uh but so basically uh we can describe uh but so basically uh we can describe
    uh but so basically uh we can describe

    this whole thing into a categorical this whole thing into a categorical this whole
    thing into a categorical

    distribution right so essentially it distribution right so essentially it distribution
    right so essentially it

    just like the transform token given the just like the transform token given the
    just like the transform token given the

    previous token which is cat uh follows a previous token which is cat uh follows
    a previous token which is cat uh follows a

    categorical distribution that can be you categorical distribution that can be
    you categorical distribution that can be you

    know uh represented by this uh know uh represented by this uh know uh represented
    by this uh

    probability probability probability

    distribution or like this vector distribution or like this vector distribution
    or like this vector

    essentially Okay. Uh and if we stack all essentially Okay. Uh and if we stack
    all essentially Okay. Uh and if we stack all

    three uh then we can apply three uh then we can apply three uh then we can apply

    hold on if we stack all three tokens and hold on if we stack all three tokens
    and hold on if we stack all three tokens and

    then you know so you just so the first'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 16
  start_sec: 910.069
  end_sec: 981.12
  text: 'then you know so you just so the first then you know so you just so the first

    row is uh I second row is love uh third row is uh I second row is love uh third
    row is uh I second row is love uh third

    row is cat uh then and then we can row is cat uh then and then we can row is cat
    uh then and then we can

    independently analyze to each token independently analyze to each token independently
    analyze to each token

    right uh then we can get basically just right uh then we can get basically just
    right uh then we can get basically just

    matrix multiplication and then you get matrix multiplication and then you get
    matrix multiplication and then you get

    the thing that you want. Uh and then the the thing that you want. Uh and then
    the the thing that you want. Uh and then the

    categorical probability distribution can categorical probability distribution
    can categorical probability distribution can

    also be represented as this matrix also be represented as this matrix also be
    represented as this matrix

    multiplication version of the multiplication version of the multiplication version
    of the

    representation. representation. representation.

    Okay. Any question? No question. Great. All right. So now No question. Great.
    All right. So now

    let''s build the diffusion for process let''s build the diffusion for process
    let''s build the diffusion for process

    using this definition of noise. Right. using this definition of noise. Right.
    using this definition of noise. Right.

    Uh so literally you just add a subscript Uh so literally you just add a subscript
    Uh so literally you just add a subscript

    t to everything and that''s diffusion a t to everything and that''s diffusion
    a t to everything and that''s diffusion a

    so easy. so easy. so easy.

    Um well uh the well it is pretty easy Um well uh the well it is pretty easy Um
    well uh the well it is pretty easy

    and also uh the the good thing about and also uh the the good thing about and
    also uh the the good thing about

    having this kind of transformation is having this kind of transformation is having
    this kind of transformation is

    that by induction we can not only get that by induction we can not only get'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 17
  start_sec: 981.12
  end_sec: 1031.99
  text: 'that by induction we can not only get

    like basically it''s the same thing as like basically it''s the same thing as
    like basically it''s the same thing as

    like you know two gausians added like you know two gausians added like you know
    two gausians added

    together equal to the same equal to together equal to the same equal to together
    equal to the same equal to

    another gausian. Uh this one is also another gausian. Uh this one is also another
    gausian. Uh this one is also

    like basically uh you know transforming like basically uh you know transforming
    like basically uh you know transforming

    from uh t minus 2 to t is equivalent to from uh t minus 2 to t is equivalent to
    from uh t minus 2 to t is equivalent to

    first transition from t minus2 to t first transition from t minus2 to t first
    transition from t minus2 to t

    minus one and then transition from t minus one and then transition from t minus
    one and then transition from t

    minus one to t right uh so basically you minus one to t right uh so basically
    you minus one to t right uh so basically you

    just like literally have two matrix just like literally have two matrix just like
    literally have two matrix

    multiplications right so by induction we multiplications right so by induction
    we multiplications right so by induction we

    can literally get the onestep uh you can literally get the onestep uh you can
    literally get the onestep uh you

    know transformation from time zero to know transformation from time zero to know
    transformation from time zero to

    time t to be something like this Right. time t to be something like this Right.
    time t to be something like this Right.

    So essentially just the the the the one So essentially just the the the the one
    So essentially just the the the the one

    step before jumping is like the same step before jumping is like the same step
    before jumping is like the same

    like anal like analogy to continuous like anal like analogy to continuous like
    anal like analogy to continuous

    diffusion DDPN one step four right. So diffusion DDPN one step four right. So
    diffusion DDPN one step four right. So

    this is like literally how to jump'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 18
  start_sec: 1031.99
  end_sec: 1104.07
  text: 'this is like literally how to jump this is like literally how to jump

    directly from x0 to xt is you just like directly from x0 to xt is you just like
    directly from x0 to xt is you just like

    kind of like apply this like apply this kind of like apply this like apply this
    kind of like apply this like apply this

    giant uh matrix multiplication term giant uh matrix multiplication term giant
    uh matrix multiplication term

    which you can calculate you know either which you can calculate you know either
    which you can calculate you know either

    ahead of time or in some smart ways or ahead of time or in some smart ways or
    ahead of time or in some smart ways or

    yeah stuff like that basically. yeah stuff like that basically. yeah stuff like
    that basically.

    Any questions? if you go back. if you go back.

    >> H you should uh did I not add tea? I may >> H you should uh did I not add tea?
    I may >> H you should uh did I not add tea? I may

    not add tea. Let''s see. >> So like it''s you also have like a >> So like it''s
    you also have like a

    noising schedule if you will. Yeah. >> All right. Any question? >> All right.
    Any question?

    Yeah. Yeah. Yeah.

    How do you really exactly like calculate How do you really exactly like calculate
    How do you really exactly like calculate

    beta at each time step? beta at each time step? beta at each time step?

    >> How do you exactly calculate beta is >> How do you exactly calculate beta is
    >> How do you exactly calculate beta is

    set? It''s like the same as the beta in set? It''s like the same as the beta in
    set? It''s like the same as the beta in

    DDPM. DDPM. DDPM.

    You choose it. Yeah. You choose it. Yeah. You choose it. Yeah.

    >> Why is beta? I thought it depend on >> Why is beta? I thought it depend on
    >> Why is beta? I thought it depend on

    >> Yeah. Beta t is a set schedule. The same >> Yeah. Beta t is a set schedule.
    The same >> Yeah. Beta t is a set schedule. The same

    as the beta t in uh DDPM.'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 19
  start_sec: 1104.07
  end_sec: 1180.87
  text: 'as the beta t in uh DDPM. as the beta t in uh DDPM.

    >> Yeah. Don''t worry. Everything''s gonna be Don''t worry. Everything''s gonna
    be

    simplified later on in this class. right simplified later on in this class. right
    simplified later on in this class. right

    now is the the more difficult one now is the the more difficult one now is the
    the more difficult one

    because this is from like 2021 or because this is from like 2021 or because this
    is from like 2021 or

    something. So people are still confused. something. So people are still confused.
    something. So people are still confused.

    All right. Anyway, uh any questions? >> Is this engram? What do you think? This
    >> Is this engram? What do you think? This

    is actually a good question. What is is actually a good question. What is is actually
    a good question. What is

    this? Is this What''s the difference this? Is this What''s the difference this?
    Is this What''s the difference

    between engram and this actually? depends on the tokens that come before depends
    on the tokens that come before

    it. But this doesn''t have that. it. But this doesn''t have that. it. But this
    doesn''t have that.

    >> Yeah. So, Ang needs to be neighboring uh >> Yeah. So, Ang needs to be neighboring
    uh >> Yeah. So, Ang needs to be neighboring uh

    tokens, right? And this one it can be tokens, right? And this one it can be tokens,
    right? And this one it can be

    any. any. any.

    >> Yeah. All right. Uh well, I think I run out. I don''t know. well, I think I
    run out. I don''t know.

    I''m not sure. Uh I''m not sure. Uh I''m not sure. Uh

    >> okay. Okay. >> okay. Okay. >> okay. Okay.

    All right. All right. All right. Okay. All right. All right. All right. Okay.
    All right. All right. All right. Okay.

    Um anyway, cool. Now, how do we learn Um anyway, cool. Now, how do we learn Um
    anyway, cool. Now, how do we learn

    this reverse process? Anyone have any this reverse process? Anyone have any this
    reverse process? Anyone have any

    ideas? ideas? ideas?

    What do we think? What do we think? What do we think?

    >> Yeah. >> Yeah. >> Yeah.

    >> Estimate these points and then Q'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 20
  start_sec: 1180.87
  end_sec: 1237.36
  text: '>> Estimate these points and then Q >> Estimate these points and then Q

    transpose. transpose. transpose.

    >> Yes, pretty much. And then specifically, >> Yes, pretty much. And then specifically,
    >> Yes, pretty much. And then specifically,

    which what kind of loss fun do we want which what kind of loss fun do we want
    which what kind of loss fun do we want

    to learn? Well, yeah, kind of. Well, actually we we we kind of just Well, actually
    we we we kind of just

    need to use the same elbow from DDPM need to use the same elbow from DDPM need
    to use the same elbow from DDPM

    because it''s kind of the same thing. The because it''s kind of the same thing.
    The because it''s kind of the same thing. The

    only difference is that we have only difference is that we have only difference
    is that we have

    different like different like different like

    uh I guess uh expressions for the Q''s uh I guess uh expressions for the Q''s
    uh I guess uh expressions for the Q''s

    and the P''s. And so we have the Q and and the P''s. And so we have the Q and
    and the P''s. And so we have the Q and

    that just like a you know reconstruction that just like a you know reconstruction
    that just like a you know reconstruction

    cross entropy. So we can just ignore we cross entropy. So we can just ignore we
    cross entropy. So we can just ignore we

    know how to do those. So the only thing know how to do those. So the only thing
    know how to do those. So the only thing

    we pretty much need to deal with is this we pretty much need to deal with is this
    we pretty much need to deal with is this

    this new Q, right? So how do we derive this new Q, right? So how do we derive
    this new Q, right? So how do we derive

    this new Q here? Well, it''s actually this new Q here? Well, it''s actually this
    new Q here? Well, it''s actually

    very simple. So you based it and then very simple. So you based it and then very
    simple. So you based it and then

    because you''re getting you''re marovian because you''re getting you''re marovian'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 21
  start_sec: 1237.36
  end_sec: 1295.27
  text: 'because you''re getting you''re marovian

    like everything is marovian here. So you like everything is marovian here. So
    you like everything is marovian here. So you

    can ignore the x0 here. So then this can ignore the x0 here. So then this can
    ignore the x0 here. So then this

    becomes uh xt given xt minus one. Uh and becomes uh xt given xt minus one. Uh
    and becomes uh xt given xt minus one. Uh and

    then um this is so qxt given x minus one then um this is so qxt given x minus
    one then um this is so qxt given x minus one

    times q which we know which we define times q which we know which we define times
    q which we know which we define

    and then q of xtus one given x which we and then q of xtus one given x which we
    and then q of xtus one given x which we

    also know from previous slides and also know from previous slides and also know
    from previous slides and

    similarly for the denominator um similarly for the denominator um similarly for
    the denominator um

    denominator. Yeah. Um so basically you denominator. Yeah. Um so basically you
    denominator. Yeah. Um so basically you

    just plug everything in and then you get just plug everything in and then you
    get just plug everything in and then you get

    something like this. And because this something like this. And because this something
    like this. And because this

    needs to be a function of uh xt minus needs to be a function of uh xt minus needs
    to be a function of uh xt minus

    one uh so you basically rearrange some one uh so you basically rearrange some
    one uh so you basically rearrange some

    terms and you get something that is terms and you get something that is terms
    and you get something that is

    equivalent. Um so now equivalent. Um so now equivalent. Um so now

    essentially um q of x um t minus one is essentially um q of x um t minus one is
    essentially um q of x um t minus one is

    literally just equal to um yeah the literally just equal to um yeah the literally
    just equal to um yeah the

    categorical distribution that is defined'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 22
  start_sec: 1295.27
  end_sec: 1362.48
  text: 'categorical distribution that is defined categorical distribution that is
    defined

    by this black font term here. >> Oh dot is like elementwise >> Oh dot is like
    elementwise

    multiplication. Anyway, honestly, doesn''t matter. The Anyway, honestly, doesn''t
    matter. The

    only thing that you need to know is that only thing that you need to know is that
    only thing that you need to know is that

    we can have closed form solution for we can have closed form solution for we can
    have closed form solution for

    this term. All right, so now we have this term. All right, so now we have this
    term. All right, so now we have

    that as well. So basically uh we can that as well. So basically uh we can that
    as well. So basically uh we can

    just directly parameterize it this way. just directly parameterize it this way.
    just directly parameterize it this way.

    But uh you know by DDPM we also know But uh you know by DDPM we also know But
    uh you know by DDPM we also know

    that you know a better parameterization that you know a better parameterization
    that you know a better parameterization

    you know homework one uh question six you know homework one uh question six you
    know homework one uh question six

    right better parameterization can have a right better parameterization can have
    a right better parameterization can have a

    lot of effect on your training lot of effect on your training lot of effect on
    your training

    performance. Uh so what is the best performance. Uh so what is the best performance.
    Uh so what is the best

    parameterization in this case? Like what parameterization in this case? Like what
    parameterization in this case? Like what

    what should be the training target like what should be the training target like
    what should be the training target like

    what should be the the thing that the what should be the the thing that the what
    should be the the thing that the

    neuronet network produce neuronet network produce neuronet network produce

    then then then

    >> uh >> uh >> uh

    the noise may be a little bit more the noise may be a little bit more the noise
    may be a little bit more

    difficult to define in this case. Right? difficult to define in this case. Right?'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 23
  start_sec: 1362.48
  end_sec: 1410.799
  text: 'difficult to define in this case. Right?

    What is the other thing? What is the other thing? What is the other thing?

    >> Tokens. >> Tokens. >> Tokens.

    >> The what >> The what >> The what

    >> the probability is of the tokens. the >> the probability is of the tokens.
    the >> the probability is of the tokens. the

    categorical distribution at each categorical distribution at each categorical
    distribution at each

    position. position. position.

    >> Well, that is just that, right? So, is >> Well, that is just that, right? So,
    is >> Well, that is just that, right? So, is

    there like any like easier target that there like any like easier target that
    there like any like easier target that

    we can that we can um you know, we can that we can um you know, we can that we
    can um you know,

    we have the noise prediction and we have we have the noise prediction and we have
    we have the noise prediction and we have

    >> clean prediction, right? Literally just >> clean prediction, right? Literally
    just >> clean prediction, right? Literally just

    that. Uh but basically what you can do that. Uh but basically what you can do
    that. Uh but basically what you can do

    is you can just channel your inner bay is you can just channel your inner bay
    is you can just channel your inner bay

    again. Uh and then you can basically again. Uh and then you can basically again.
    Uh and then you can basically

    just like decompose uh you know your just like decompose uh you know your just
    like decompose uh you know your

    target into or like your objective or target into or like your objective or target
    into or like your objective or

    not objective your your uh you know the not objective your your uh you know the
    not objective your your uh you know the

    thing that you''re supposed to predict thing that you''re supposed to predict
    thing that you''re supposed to predict

    into like the four process times the into like the four process times the into
    like the four process times the

    clean data estimation or the clean data clean data estimation or the clean data
    clean data estimation or the clean data

    prediction right so literally you need prediction right so literally you need'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 24
  start_sec: 1410.799
  end_sec: 1458.559
  text: 'prediction right so literally you need

    to only you only need to predict the to only you only need to predict the to only
    you only need to predict the

    logist of the final clean output given logist of the final clean output given
    logist of the final clean output given

    your current erh like noisy input and your current erh like noisy input and your
    current erh like noisy input and

    then everything just be calculated ated then everything just be calculated ated
    then everything just be calculated ated

    by you know like like the KL divergence by you know like like the KL divergence
    by you know like like the KL divergence

    between the two and uh also uh in the between the two and uh also uh in the between
    the two and uh also uh in the

    paper they also said oh actually uh you paper they also said oh actually uh you
    paper they also said oh actually uh you

    can also add another cross entropy loss can also add another cross entropy loss
    can also add another cross entropy loss

    just like just just like the BERT just like just just like the BERT just like
    just just like the BERT

    essentially and then it''s going to essentially and then it''s going to essentially
    and then it''s going to

    improve the performance a little bit. So improve the performance a little bit.
    So improve the performance a little bit. So

    if you put everything together, we got if you put everything together, we got
    if you put everything together, we got

    the first uh like proper discrete the first uh like proper discrete the first
    uh like proper discrete

    diffusion like so it''s actually the the diffusion like so it''s actually the
    the diffusion like so it''s actually the the

    noising process and everything happens noising process and everything happens
    noising process and everything happens

    in the discrete space and this is what in the discrete space and this is what
    in the discrete space and this is what

    we call a discree uh dn noising we call a discree uh dn noising we call a discree
    uh dn noising

    diffusion model because we''re 3D so it''s diffusion model because we''re 3D so
    it''s diffusion model because we''re 3D so it''s

    a D3PM. a D3PM.'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 25
  start_sec: 1458.559
  end_sec: 1517.039
  text: 'a D3PM.

    All right, any questions about D3PM? Yes, Yes,

    >> this won''t have like an equivalence to >> this won''t have like an equivalence
    to >> this won''t have like an equivalence to

    like score matching, right? Because of like score matching, right? Because of
    like score matching, right? Because of

    the discrete space, the discrete space, the discrete space,

    >> we have not talked about score matching >> we have not talked about score matching
    >> we have not talked about score matching

    yet. Uh but we''re going to talk about it yet. Uh but we''re going to talk about
    it yet. Uh but we''re going to talk about it

    next. Any other questions before we move next. Any other questions before we move
    next. Any other questions before we move

    on to score matching? on to score matching? on to score matching?

    >> Yeah. >> Oh, you cannot do variable length here. >> Oh, you cannot do variable
    length here.

    Yeah. Yeah. Oh, yeah. We''re g we were Yeah. Yeah. Oh, yeah. We''re g we were
    Yeah. Yeah. Oh, yeah. We''re g we were

    gonna talk about it in next class but gonna talk about it in next class but gonna
    talk about it in next class but

    they actually fix this kind of fix it I they actually fix this kind of fix it
    I they actually fix this kind of fix it I

    guess u but but but but but like using guess u but but but but but like using
    guess u but but but but but like using

    some like hacks I guess u but yeah one some like hacks I guess u but yeah one
    some like hacks I guess u but yeah one

    downside about diffusion language model downside about diffusion language model
    downside about diffusion language model

    is that everything needs to be trained is that everything needs to be trained
    is that everything needs to be trained

    in a fixed length uh scenario in a fixed length uh scenario in a fixed length
    uh scenario

    unfortunately yes it''s not variable yeah unfortunately yes it''s not variable
    yeah unfortunately yes it''s not variable yeah

    >> autogressive models as some kind of uh >> autogressive models as some kind
    of uh >> autogressive models as some kind of uh

    like discrete diffusion models like discrete diffusion models'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 26
  start_sec: 1517.039
  end_sec: 1593.36
  text: 'like discrete diffusion models

    >> great question and the answer is Yes. >> great question and the answer is Yes.
    >> great question and the answer is Yes.

    And we''re going to talk about it next And we''re going to talk about it next
    And we''re going to talk about it next

    class actually. Yeah. But uh allergy. class actually. Yeah. But uh allergy. class
    actually. Yeah. But uh allergy.

    All right. Actually, I don''t even know All right. Actually, I don''t even know
    All right. Actually, I don''t even know

    if I have non-allergy things anymore, if I have non-allergy things anymore, if
    I have non-allergy things anymore,

    but let''s see. All right. I give up. All right. I give up.

    Academic. Dang. Why you guys Nobody''s graduating Dang. Why you guys Nobody''s
    graduating

    soon or something. soon or something. soon or something.

    All right. Cool. Cool. Cool. All right. So, right. Cool. Cool. Cool. All right.
    So,

    you know, as people have been asking, you know, as people have been asking, you
    know, as people have been asking,

    uh, so we covered like one aspect of so we covered like one aspect of

    discrete diffusion which is like kind of discrete diffusion which is like kind
    of discrete diffusion which is like kind of

    corresponding to the process of adding corresponding to the process of adding
    corresponding to the process of adding

    noise and learning to d noise, right? noise and learning to d noise, right? noise
    and learning to d noise, right?

    And then we basically just um, you know And then we basically just um, you know
    And then we basically just um, you know

    define our noise in the categorical define our noise in the categorical define
    our noise in the categorical

    distribution. So we get that covered. Uh distribution. So we get that covered.
    Uh distribution. So we get that covered. Uh

    now what about score function right like now what about score function right like
    now what about score function right like

    the score functions the whole concept the score functions the whole concept the
    score functions the whole concept

    seems really wrong here but we can do seems really wrong here but we can do seems
    really wrong here but we can do

    that. Yeah that. Yeah that. Yeah

    >> previous >> previous >> previous

    fixed length. fixed length.'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 27
  start_sec: 1593.36
  end_sec: 1644.4
  text: 'fixed length.

    >> Yeah it''s fixed length. Everything is >> Yeah it''s fixed length. Everything
    is >> Yeah it''s fixed length. Everything is

    fixed length. Yeah. fixed length. Yeah. fixed length. Yeah.

    >> It''s the same for everything. >> It''s the same for everything. >> It''s the
    same for everything.

    Yeah. So maybe it''s fine but like it Yeah. So maybe it''s fine but like it Yeah.
    So maybe it''s fine but like it

    just like the well like formulation wise just like the well like formulation wise
    just like the well like formulation wise

    it so like mathematically it has to be it so like mathematically it has to be
    it so like mathematically it has to be

    uh like fixed length whereas if you do uh like fixed length whereas if you do
    uh like fixed length whereas if you do

    auto reggressive mathematically it auto reggressive mathematically it auto reggressive
    mathematically it

    doesn''t have to right it''s just that doesn''t have to right it''s just that
    doesn''t have to right it''s just that

    when we''re training a transformer the when we''re training a transformer the
    when we''re training a transformer the

    transformer is fixed length. Yeah. So transformer is fixed length. Yeah. So transformer
    is fixed length. Yeah. So

    like in transformer it doesn''t really like in transformer it doesn''t really
    like in transformer it doesn''t really

    matter that much I guess but yeah matter that much I guess but yeah matter that
    much I guess but yeah

    but it''s still we''re going to talk about but it''s still we''re going to talk
    about but it''s still we''re going to talk about

    how like it''s more in it''s actually not how like it''s more in it''s actually
    not how like it''s more in it''s actually not

    as efficient uh and how people are as efficient uh and how people are as efficient
    uh and how people are

    trying to solve it um next class though. trying to solve it um next class though.
    trying to solve it um next class though.

    Yeah. Any other questions before me Yeah. Any other questions before me Yeah.
    Any other questions before me

    before we move on? before we move on? before we move on?

    Alrighty. Okay. So h just a reminder Alrighty. Okay. So h just a reminder'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 28
  start_sec: 1644.4
  end_sec: 1690.64
  text: 'Alrighty. Okay. So h just a reminder

    what is a uh what is a continuous score what is a uh what is a continuous score
    what is a uh what is a continuous score

    and why is it weird to think about score and why is it weird to think about score
    and why is it weird to think about score

    functions in the discrete space. So functions in the discrete space. So functions
    in the discrete space. So

    continuously if if your status space is continuously if if your status space is
    continuously if if your status space is

    a continuous space like a 2D plane right a continuous space like a 2D plane right
    a continuous space like a 2D plane right

    uh then the score function is like the uh then the score function is like the
    uh then the score function is like the

    gradient uh that goes towards the higher gradient uh that goes towards the higher
    gradient uh that goes towards the higher

    likelihood region right so you just like likelihood region right so you just like
    likelihood region right so you just like

    usually and then you just like follow usually and then you just like follow usually
    and then you just like follow

    the flow uh so to speak whereas if the flow uh so to speak whereas if the flow
    uh so to speak whereas if

    you''re talking about a discreet um like you''re talking about a discreet um like
    you''re talking about a discreet um like

    score I guess what you do is you do not score I guess what you do is you do not
    score I guess what you do is you do not

    you cannot really flow continuously you cannot really flow continuously you cannot
    really flow continuously

    anymore right what you can do is you anymore right what you can do is you anymore
    right what you can do is you

    have like sort like three disconnected have like sort like three disconnected
    have like sort like three disconnected

    points and you''re low key just like points and you''re low key just like points
    and you''re low key just like

    jumping between the points. So there''s jumping between the points. So there''s
    jumping between the points. So there''s

    no continuous flow anymore. There''s no no continuous flow anymore. There''s no'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 29
  start_sec: 1690.64
  end_sec: 1736.08
  text: 'no continuous flow anymore. There''s no

    gradient like you cannot like really do gradient like you cannot like really do
    gradient like you cannot like really do

    any gradient stuff anymore here, right? any gradient stuff anymore here, right?
    any gradient stuff anymore here, right?

    So that''s like really weird. Uh so how So that''s like really weird. Uh so how
    So that''s like really weird. Uh so how

    do we do that, right? So essentially but do we do that, right? So essentially
    but do we do that, right? So essentially but

    but like basically if you think about it but like basically if you think about
    it but like basically if you think about it

    just just if you uh if you vibe with it just just if you uh if you vibe with it
    just just if you uh if you vibe with it

    uh you know the continuous score is uh you know the continuous score is uh you
    know the continuous score is

    basically saying that like compare my basically saying that like compare my basically
    saying that like compare my

    likelihood with my neighbors with like likelihood with my neighbors with like
    likelihood with my neighbors with like

    my surrounding and uh if they are higher my surrounding and uh if they are higher
    my surrounding and uh if they are higher

    if if my neighbors has higher likelihood if if my neighbors has higher likelihood
    if if my neighbors has higher likelihood

    than me then I will flow to them than me then I will flow to them than me then
    I will flow to them

    otherwise they flow to me right so this otherwise they flow to me right so this
    otherwise they flow to me right so this

    is like the same kind of like so we if is like the same kind of like so we if
    is like the same kind of like so we if

    We follow the same vibe as that like We follow the same vibe as that like We follow
    the same vibe as that like

    just like comparing with my neighbors just like comparing with my neighbors just
    like comparing with my neighbors

    type of thing. Uh which is not a healthy type of thing. Uh which is not a healthy'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 30
  start_sec: 1736.08
  end_sec: 1781.679
  text: 'type of thing. Uh which is not a healthy

    thing to do but like you know just for thing to do but like you know just for
    thing to do but like you know just for

    the sake of the class anyway um you know the sake of the class anyway um you know
    the sake of the class anyway um you know

    it if uh like so in discrete case what it if uh like so in discrete case what
    it if uh like so in discrete case what

    we do is we don''t flow to them we just we do is we don''t flow to them we just
    we do is we don''t flow to them we just

    directly jump. So like if your neighbors directly jump. So like if your neighbors
    directly jump. So like if your neighbors

    uh has higher likelihood than you then uh has higher likelihood than you then
    uh has higher likelihood than you then

    you you you

    jump to them instead of float. But like jump to them instead of float. But like
    jump to them instead of float. But like

    how to describe this jumping rate, how to describe this jumping rate, how to describe
    this jumping rate,

    right? This like this jumping frequency right? This like this jumping frequency
    right? This like this jumping frequency

    I guess. Uh then what you can do is I guess. Uh then what you can do is I guess.
    Uh then what you can do is

    literally basically have something so literally basically have something so literally
    basically have something so

    that the discrete score quote unquote that the discrete score quote unquote that
    the discrete score quote unquote

    the score is sort of just a comparison the score is sort of just a comparison
    the score is sort of just a comparison

    between the likelihood at your current between the likelihood at your current
    between the likelihood at your current

    point and the likelihood at the point point and the likelihood at the point point
    and the likelihood at the point

    that you''re going to jump to. So uh that you''re going to jump to. So uh that
    you''re going to jump to. So uh

    basically what people does is that they basically what people does is that they'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 31
  start_sec: 1781.679
  end_sec: 1849.6
  text: 'basically what people does is that they

    define something called uh the concrete define something called uh the concrete
    define something called uh the concrete

    score where it''s literally just the score where it''s literally just the score
    where it''s literally just the

    probability or the probability ratio probability or the probability ratio probability
    or the probability ratio

    between the point that you''re jumping to between the point that you''re jumping
    to between the point that you''re jumping to

    and the point that you''re currently at. and the point that you''re currently
    at. and the point that you''re currently at.

    Does it make sense people? >> Yeah.

    wouldn''t be able to just jump to any wouldn''t be able to just jump to any wouldn''t
    be able to just jump to any

    neighbors because there''s no like neighbors because there''s no like neighbors
    because there''s no like

    inherent ordering between the tokens, inherent ordering between the tokens, inherent
    ordering between the tokens,

    right? right? right?

    >> Um that is still fine. >> Um that is still fine. >> Um that is still fine.

    >> And we''re going to see why. Yeah. Okay. >> And we''re going to see why. Yeah.
    Okay. >> And we''re going to see why. Yeah. Okay.

    Uh let yeah >> you could be definitely which is why you >> you could be definitely
    which is why you

    need to define your trans transition need to define your trans transition need
    to define your trans transition

    like clearly essentially. But anyway, like clearly essentially. But anyway, like
    clearly essentially. But anyway,

    let let me let me go through a little let let me let me go through a little let
    let me let me go through a little

    bit more of the map. Yeah. bit more of the map. Yeah. bit more of the map. Yeah.

    >> To look at the subgradient when compared >> To look at the subgradient when
    compared >> To look at the subgradient when compared

    to this to this to this

    >> uh you the the the gradient >> uh you the the the gradient >> uh you the the
    the gradient

    >> the subgradient >> the network generalization >> the network generalization

    >> I see I have no idea actually but >> I see I have no idea actually but >> I
    see I have no idea actually but

    apparently apparently'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 32
  start_sec: 1849.6
  end_sec: 1908.23
  text: 'apparently

    uh if you read this particular paper uh if you read this particular paper uh if
    you read this particular paper

    they have some connections to something they have some connections to something
    they have some connections to something

    but I''m not entirely sure unfortunately. but I''m not entirely sure unfortunately.
    but I''m not entirely sure unfortunately.

    Sorry. Okay. Anyway, Sorry. Okay. Anyway, Sorry. Okay. Anyway,

    uh so uh so uh so

    uh another piece of the thing that we''re uh another piece of the thing that we''re
    uh another piece of the thing that we''re

    missing here is that in continuous missing here is that in continuous missing
    here is that in continuous

    score-based models, not only that we um score-based models, not only that we um
    score-based models, not only that we um

    like model everything in score function, like model everything in score function,
    like model everything in score function,

    we also represent everything in a we also represent everything in a we also represent
    everything in a

    continuous time SD or OD, right? Uh so continuous time SD or OD, right? Uh so
    continuous time SD or OD, right? Uh so

    what what does even mean to have a what what does even mean to have a what what
    does even mean to have a

    continuous time discrete jump? Uh well, continuous time discrete jump? Uh well,
    continuous time discrete jump? Uh well,

    essentially there is this other notion. essentially there is this other notion.
    essentially there is this other notion.

    It''s called uh continuous time markoff It''s called uh continuous time markoff
    It''s called uh continuous time markoff

    chain or CTMC. And what it does is chain or CTMC. And what it does is chain or
    CTMC. And what it does is

    basically you still have some sort of basically you still have some sort of basically
    you still have some sort of

    like uh transition matrix. Uh but like like uh transition matrix. Uh but like
    like uh transition matrix. Uh but like

    basically but but now this transition basically but but now this transition basically
    but but now this transition

    matrix so sort of like represents some matrix so sort of like represents some
    matrix so sort of like represents some

    like instantaneous rate essentially like instantaneous rate essentially like instantaneous
    rate essentially

    people actually call it a rate matrix.'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 33
  start_sec: 1908.23
  end_sec: 1963.75
  text: 'people actually call it a rate matrix. people actually call it a rate matrix.

    So it''s a instantaneous rate to jump So it''s a instantaneous rate to jump So
    it''s a instantaneous rate to jump

    like just just just think about if you like just just just think about if you
    like just just just think about if you

    just discretize your the the trend the just discretize your the the trend the
    just discretize your the the trend the

    evolution like infiniteesimally small evolution like infiniteesimally small evolution
    like infiniteesimally small

    and uh the probability to jump from one and uh the probability to jump from one
    and uh the probability to jump from one

    state uh to the next infiniteimally state uh to the next infiniteimally state
    uh to the next infiniteimally

    small steps can be written as this thing small steps can be written as this thing
    small steps can be written as this thing

    which is basically which is basically which is basically

    your rate times your infinite decimally your rate times your infinite decimally
    your rate times your infinite decimally

    small time. small time. small time.

    uh uh if so you''re jumping to another uh uh if so you''re jumping to another
    uh uh if so you''re jumping to another

    point point point

    uh you know with the rate times infinite uh you know with the rate times infinite
    uh you know with the rate times infinite

    decimal small time and then the rate or decimal small time and then the rate or
    decimal small time and then the rate or

    like the probability that you''re staying like the probability that you''re staying
    like the probability that you''re staying

    at your current point is literally just at your current point is literally just
    at your current point is literally just

    one minus whatever that is left whatever one minus whatever that is left whatever
    one minus whatever that is left whatever

    that is sum over all the other states. that is sum over all the other states.
    that is sum over all the other states.

    Okay. Um, so essentially if you if you Okay. Um, so essentially if you if you
    Okay. Um, so essentially if you if you

    want something to satisfy this whole want something to satisfy this whole want
    something to satisfy this whole

    thing, then you''re actually basically if'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 34
  start_sec: 1963.75
  end_sec: 2007.76
  text: 'thing, then you''re actually basically if thing, then you''re actually basically
    if

    you do the math then then then you''re you do the math then then then you''re
    you do the math then then then you''re

    actually going to get like the sort of actually going to get like the sort of
    actually going to get like the sort of

    like the the rate to stay at the current like the the rate to stay at the current
    like the the rate to stay at the current

    state is the same as the negative of all state is the same as the negative of
    all state is the same as the negative of all

    the other rate combined. So basically the other rate combined. So basically the
    other rate combined. So basically

    just like just imagine how like remember just like just imagine how like remember
    just like just imagine how like remember

    how we have like a like a conservation how we have like a like a conservation
    how we have like a like a conservation

    of mass, right? like basically this the of mass, right? like basically this the
    of mass, right? like basically this the

    the mass of water or like the volume of the mass of water or like the volume of
    the mass of water or like the volume of

    the water or the or the sum of the water or the or the sum of the water or the
    or the sum of

    probability stays at one right so probability stays at one right so probability
    stays at one right so

    basically essentially all the rate you basically essentially all the rate you
    basically essentially all the rate you

    should cancel out each other at the end should cancel out each other at the end
    should cancel out each other at the end

    so that''s why everything should sum up so that''s why everything should sum up
    so that''s why everything should sum up

    to zero in the rate space to zero in the rate space to zero in the rate space

    to be like a fully connected everyone to be like a fully connected everyone to
    be like a fully connected everyone

    what is what is what is

    >> uh yeah like so like basically >> uh yeah like so like basically >> uh yeah
    like so like basically

    everything everything'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 35
  start_sec: 2007.76
  end_sec: 2062.639
  text: 'everything

    well you can represent everything in a well you can represent everything in a
    well you can represent everything in a

    fully connected graph and then assign fully connected graph and then assign fully
    connected graph and then assign

    zero rate right zero rate right zero rate right

    yeah yeah yeah

    so it''s going to be the same thing so it''s going to be the same thing so it''s
    going to be the same thing

    essentially essentially essentially

    okay but basically we can also write okay but basically we can also write okay
    but basically we can also write

    this turns out we can also write this this turns out we can also write this this
    turns out we can also write this

    thing into OD and this OD can be thing into OD and this OD can be thing into OD
    and this OD can be

    represented as this thing uh and represented as this thing uh and represented
    as this thing uh and

    basically uh going in reverse uh basically uh going in reverse uh basically uh
    going in reverse uh

    okay so basically now I''m so sorry for okay so basically now I''m so sorry for
    okay so basically now I''m so sorry for

    the confusion of the notation but now Q the confusion of the notation but now
    Q the confusion of the notation but now Q

    R means the reverse time in in R means the reverse time in in R means the reverse
    time in in

    instantaneous instantaneous instantaneous

    rate. Okay, so it''s not the the the the rate. Okay, so it''s not the the the
    the rate. Okay, so it''s not the the the the

    product anymore. It''s the reversed rate. product anymore. It''s the reversed
    rate. product anymore. It''s the reversed rate.

    Uh and then like basically if you do the Uh and then like basically if you do
    the Uh and then like basically if you do the

    math correctly bas why why are you doing math correctly bas why why are you doing
    math correctly bas why why are you doing

    this way is because of detail balance. this way is because of detail balance.
    this way is because of detail balance.

    So if you want your chain to satisfy So if you want your chain to satisfy'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 36
  start_sec: 2062.639
  end_sec: 2119.44
  text: 'So if you want your chain to satisfy

    detail balance you''re going to get this detail balance you''re going to get this
    detail balance you''re going to get this

    thing so that your chain is reversible, thing so that your chain is reversible,
    thing so that your chain is reversible,

    right? Uh and then uh this is just some right? Uh and then uh this is just some
    right? Uh and then uh this is just some

    marco chain things but basically if you marco chain things but basically if you
    marco chain things but basically if you

    want your chain to be reversible you want your chain to be reversible you want
    your chain to be reversible you

    need to satisfy detail balance. Detail need to satisfy detail balance. Detail
    need to satisfy detail balance. Detail

    balance is going to give you this balance is going to give you this balance is
    going to give you this

    equation and uh equation and uh equation and uh

    we have our concrete score in this in we have our concrete score in this in we
    have our concrete score in this in

    this equation. Uh so long story short this equation. Uh so long story short this
    equation. Uh so long story short

    you need to learn the concrete score. you need to learn the concrete score. you
    need to learn the concrete score.

    Yeah this is like the only thing that Yeah this is like the only thing that Yeah
    this is like the only thing that

    you need to remember from all of these you need to remember from all of these
    you need to remember from all of these

    math. It''s like basically we need to math. It''s like basically we need to math.
    It''s like basically we need to

    learn the concrete score in order to get learn the concrete score in order to
    get learn the concrete score in order to get

    the score-based model equivalence of the score-based model equivalence of the
    score-based model equivalence of

    discrete diffusion. discrete diffusion. discrete diffusion.

    Now how to learn a concrete score? What Now how to learn a concrete score? What
    Now how to learn a concrete score? What

    do we think? There should be a very easy answer, There should be a very easy answer,

    right? I see everyone''s confused by how this'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 37
  start_sec: 2119.44
  end_sec: 2208.47
  text: 'I see everyone''s confused by how this

    whole thing but we need basically we whole thing but we need basically we whole
    thing but we need basically we

    need a neuronet network to predict this need a neuronet network to predict this
    need a neuronet network to predict this

    thing. thing. thing.

    >> Yeah. >> Yeah.

    >> Distribution over all the >> Distribution over all the >> Distribution over
    all the

    >> yes learn the distribution will be >> yes learn the distribution will be >>
    yes learn the distribution will be

    better. We''re going to talk about it better. We''re going to talk about it better.
    We''re going to talk about it

    later. But uh there''s a there''s a even later. But uh there''s a there''s a even
    later. But uh there''s a there''s a even

    easier way. You haven''t got my easier way. You haven''t got my easier way. You
    haven''t got my

    blessings, have you? Have you got got my blessings, have you? Have you got got
    my blessings, have you? Have you got got my

    blessings yet? >> Get get richer. Get get good grade, I >> Get get richer. Get
    get good grade, I

    guess. guess. guess.

    >> Good grade. Oh man. Okay. >> Good grade. Oh man. Okay. >> Good grade. Oh man.
    Okay.

    Um, this is no allergy version. Anyway, Um, this is no allergy version. Anyway,
    Um, this is no allergy version. Anyway,

    okay. What else? There should be a super okay. What else? There should be a super
    okay. What else? There should be a super

    easy easy easy

    version. that consists of a loss function that we that consists of a loss function
    that we

    use for this entire class. What What

    >> did you say? >> did you say? >> did you say?

    >> Elbow. Yeah. But also L2, right? You can just Yeah. But also L2, right? You
    can just

    L2 it. Yeah. So you can do concrete score Yeah. So you can do concrete score

    matching instead of score matching, matching instead of score matching, matching
    instead of score matching,

    right? And the score matching is right? And the score matching is right? And the
    score matching is

    literally L2 loss between your predicted literally L2 loss between your predicted
    literally L2 loss between your predicted

    score versus your uh you know your your'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 38
  start_sec: 2208.47
  end_sec: 2267.92
  text: 'score versus your uh you know your your score versus your uh you know your
    your

    your your your real score. And you your your your real score. And you your your
    your real score. And you

    literally just do this, right? L2 score literally just do this, right? L2 score
    literally just do this, right? L2 score

    L2 between your predicted concrete score L2 between your predicted concrete score
    L2 between your predicted concrete score

    versus your real score. versus your real score. versus your real score.

    Is there any problem with this? What do Is there any problem with this? What do
    Is there any problem with this? What do

    we think? >> well we do know we we we we could >> well we do know we we we we
    could

    construct this. construct this. construct this.

    >> Yeah. Well there there there is a way to >> Yeah. Well there there there is
    a way to >> Yeah. Well there there there is a way to

    construct this I guess if if if you construct this I guess if if if you construct
    this I guess if if if you

    want. Yeah want. Yeah want. Yeah

    >> infeasible because of the number of >> infeasible because of the number of
    >> infeasible because of the number of

    combinations of tokens. combinations of tokens. combinations of tokens.

    Um not quite not quite uh but but but Um not quite not quite uh but but but Um
    not quite not quite uh but but but

    there''s some actually I just tell you there''s some actually I just tell you
    there''s some actually I just tell you

    guys uh basically the biggest problem is guys uh basically the biggest problem
    is guys uh basically the biggest problem is

    that you actually um so like the that you actually um so like the that you actually
    um so like the

    probability ratio here should always be probability ratio here should always be
    probability ratio here should always be

    positive because it''s a positive number positive because it''s a positive number
    positive because it''s a positive number

    divided by a positive number or a divided by a positive number or a divided by
    a positive number or a

    non-zero number divided by a non-zero non-zero number divided by a non-zero'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 39
  start_sec: 2267.92
  end_sec: 2315.51
  text: 'non-zero number divided by a non-zero

    number or like or sorry non- negative number or like or sorry non- negative number
    or like or sorry non- negative

    number divided by a non- negative number number divided by a non- negative number
    number divided by a non- negative number

    right but uh as if we assume like full right but uh as if we assume like full
    right but uh as if we assume like full

    support then it''s a not then it''s support then it''s a not then it''s support
    then it''s a not then it''s

    positive number divided by positive positive number divided by positive positive
    number divided by positive

    number but the problem is that there''s number but the problem is that there''s
    number but the problem is that there''s

    no way to enforce that right in this no way to enforce that right in this no way
    to enforce that right in this

    loss function. So negative if you loss function. So negative if you loss function.
    So negative if you

    predict the likelihood ratio to be predict the likelihood ratio to be predict
    the likelihood ratio to be

    negative.5 negative.5 negative.5

    on a loss function it may seems fine on a loss function it may seems fine on a
    loss function it may seems fine

    right because it''s like maybe it''s like right because it''s like maybe it''s
    like right because it''s like maybe it''s like

    negative.5 versus ne 0.2 two. So the negative.5 versus ne 0.2 two. So the negative.5
    versus ne 0.2 two. So the

    loss function is actually quite small. loss function is actually quite small.
    loss function is actually quite small.

    Like the loss is actually quite small, Like the loss is actually quite small,
    Like the loss is actually quite small,

    but you are actually predicting but you are actually predicting but you are actually
    predicting

    something that''s like super super wrong. something that''s like super super wrong.
    something that''s like super super wrong.

    You''re actually predicting something You''re actually predicting something You''re
    actually predicting something

    that''s invalid. So this is one thing. that''s invalid. So this is one thing.
    that''s invalid. So this is one thing.

    >> Yeah. Yeah. Yeah. Yeah. Very good. Very >> Yeah. Yeah. Yeah. Yeah. Very good.
    Very >> Yeah. Yeah. Yeah. Yeah. Very good. Very

    good. Exactly. That''s exactly correct.'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 40
  start_sec: 2315.51
  end_sec: 2360.4
  text: 'good. Exactly. That''s exactly correct. good. Exactly. That''s exactly correct.

    Um uh the other thing is that yeah, you Um uh the other thing is that yeah, you
    Um uh the other thing is that yeah, you

    you may notice that the like the you may notice that the like the you may notice
    that the like the

    denominator gets small then the thing denominator gets small then the thing denominator
    gets small then the thing

    explode, right? And the other thing is explode, right? And the other thing is
    explode, right? And the other thing is

    that a lot of you guys have said that in that a lot of you guys have said that
    in that a lot of you guys have said that in

    your um homework. MSE is just like not a your um homework. MSE is just like not
    a your um homework. MSE is just like not a

    great metric in general for distribution great metric in general for distribution
    great metric in general for distribution

    matching. Um so what do we do? Okay, matching. Um so what do we do? Okay, matching.
    Um so what do we do? Okay,

    let''s derive a better loss function let''s derive a better loss function let''s
    derive a better loss function

    here. Okay, so basically if you think here. Okay, so basically if you think here.
    Okay, so basically if you think

    about it, right? Uh the reverse Q about it, right? Uh the reverse Q about it,
    right? Uh the reverse Q

    because we need to satisfy detail because we need to satisfy detail because we
    need to satisfy detail

    balance. This is how how this is what we balance. This is how how this is what
    we balance. This is how how this is what we

    derived, right? the reverse the uh rate derived, right? the reverse the uh rate
    derived, right? the reverse the uh rate

    equal to some base rate times the ratio equal to some base rate times the ratio
    equal to some base rate times the ratio

    right so the base rate is set so just right so the base rate is set so just right
    so the base rate is set so just

    like a like a like a like a like a what like a like a like a like a like a what'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 41
  start_sec: 2360.4
  end_sec: 2406.0
  text: 'like a like a like a like a like a what

    we call uh constant so let''s just ignore we call uh constant so let''s just ignore
    we call uh constant so let''s just ignore

    that for now so we basically we can that for now so we basically we can that for
    now so we basically we can

    represent this like frequency of jumping represent this like frequency of jumping
    represent this like frequency of jumping

    like if you want to describe a frequency like if you want to describe a frequency
    like if you want to describe a frequency

    of something happening in a discrete of something happening in a discrete of something
    happening in a discrete

    space right then the the first uh space right then the the first uh space right
    then the the first uh

    distribution that you should think of is distribution that you should think of
    is distribution that you should think of is

    the pson distribution. By the way, I the pson distribution. By the way, I the
    pson distribution. By the way, I

    don''t actually know if they derive it don''t actually know if they derive it
    don''t actually know if they derive it

    this way. This is sort of like my this way. This is sort of like my this way.
    This is sort of like my

    derivation and didn''t really check their derivation and didn''t really check
    their derivation and didn''t really check their

    derivation, but I think it''s it''s okay. derivation, but I think it''s it''s
    okay. derivation, but I think it''s it''s okay.

    It''s going to work. Trust me. Okay. It''s going to work. Trust me. Okay. It''s
    going to work. Trust me. Okay.

    Anyway, point being so let''s just like Anyway, point being so let''s just like
    Anyway, point being so let''s just like

    define uh the you know the the the the define uh the you know the the the the
    define uh the you know the the the the

    the the the

    data distribution and the predicted data distribution and the predicted data distribution
    and the predicted

    distribution as some person. Okay. And distribution as some person. Okay. And
    distribution as some person. Okay. And

    then the person is going to be this then the person is going to be this'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 42
  start_sec: 2406.0
  end_sec: 2454.72
  text: 'then the person is going to be this

    thing, right? So what you do is you thing, right? So what you do is you thing,
    right? So what you do is you

    essentially so K is like you you jump to essentially so K is like you you jump
    to essentially so K is like you you jump to

    you know you the the jumping event you know you the the jumping event you know
    you the the jumping event

    essentially and the basically the KL essentially and the basically the KL essentially
    and the basically the KL

    divergence between two person is plug in divergence between two person is plug
    in divergence between two person is plug in

    the formula equal to this and then this the formula equal to this and then this
    the formula equal to this and then this

    thing is basically uh if you cancel out thing is basically uh if you cancel out
    thing is basically uh if you cancel out

    everything that you can cancel uh it''s everything that you can cancel uh it''s
    everything that you can cancel uh it''s

    going to become something like this and going to become something like this and
    going to become something like this and

    then because this is a summation of two then because this is a summation of two
    then because this is a summation of two

    parts uh so you can break it break it up parts uh so you can break it break it
    up parts uh so you can break it break it up

    and uh this summation here. So basically and uh this summation here. So basically
    and uh this summation here. So basically

    and then you you you you move everything and then you you you you move everything
    and then you you you you move everything

    that is not relevant to the to to the to that is not relevant to the to to the
    to that is not relevant to the to to the to

    the to K outside of the summation and the to K outside of the summation and the
    to K outside of the summation and

    then this part becomes one uh s minus r then this part becomes one uh s minus
    r'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 43
  start_sec: 2454.72
  end_sec: 2497.599
  text: 'then this part becomes one uh s minus r

    uh times the sum of all the possible all uh times the sum of all the possible
    all uh times the sum of all the possible all

    the probabilities and then this one is the probabilities and then this one is
    the probabilities and then this one is

    the log minus the other log times the the log minus the other log times the the
    log minus the other log times the

    expectation essentially right so the sum expectation essentially right so the
    sum expectation essentially right so the sum

    of probability equals one the the of probability equals one the the of probability
    equals one the the

    expectation of a hor distribution equals expectation of a hor distribution equals
    expectation of a hor distribution equals

    the rate. So it''s R right and then the rate. So it''s R right and then the rate.
    So it''s R right and then

    basically and then you can ignore all basically and then you can ignore all basically
    and then you can ignore all

    the things that is not relevant to your the things that is not relevant to your
    the things that is not relevant to your

    theta to your learning to your parameter theta to your learning to your parameter
    theta to your learning to your parameter

    then you get something like this right then you get something like this right
    then you get something like this right

    does it make sense yeah does it make sense yeah does it make sense yeah

    >> use is there any reason apart from the >> use is there any reason apart from
    the >> use is there any reason apart from the

    fact that you want to enforce the fact that you want to enforce the fact that
    you want to enforce the

    exponential is that the reason exponential is that the reason exponential is that
    the reason

    >> that is part of the that is literally >> that is part of the that is literally
    >> that is part of the that is literally

    yeah that is part of the reason it gives yeah that is part of the reason it gives
    yeah that is part of the reason it gives

    us something that is that has that has us something that is that has that has'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 44
  start_sec: 2497.599
  end_sec: 2540.15
  text: 'us something that is that has that has

    exponential in it and also literally exponential in it and also literally exponential
    in it and also literally

    right the the the easiest right the the the easiest right the the the easiest

    uh distribution that you can think of to uh distribution that you can think of
    to uh distribution that you can think of to

    represent the rate of something represent the rate of something represent the
    rate of something

    happening is in a discrete space is happening is in a discrete space is happening
    is in a discrete space is

    person right so okay but like I said I person right so okay but like I said I
    person right so okay but like I said I

    don''t know if this is like the official don''t know if this is like the official
    don''t know if this is like the official

    derivation that they did this is derivation that they did this is derivation that
    they did this is

    something you know that I did but I something you know that I did but I something
    you know that I did but I

    think it works anyway we get to the same think it works anyway we get to the same
    think it works anyway we get to the same

    thing this is a screenshot from the thing this is a screenshot from the thing
    this is a screenshot from the

    paper don''t worry uh but yeah but paper don''t worry uh but yeah but paper don''t
    worry uh but yeah but

    basically this is a paper uh that that basically this is a paper uh that that
    basically this is a paper uh that that

    the paper some paper defined uh this the paper some paper defined uh this the
    paper some paper defined uh this

    loss called the the score entropy loss loss called the the score entropy loss
    loss called the the score entropy loss

    because it resembles an entropy, you because it resembles an entropy, you because
    it resembles an entropy, you

    know, uh and then so basically what''s know, uh and then so basically what''s
    know, uh and then so basically what''s

    happening is literally the same thing, happening is literally the same thing,
    happening is literally the same thing,

    right? So you the the S minus the'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 45
  start_sec: 2540.15
  end_sec: 2592.24
  text: 'right? So you the the S minus the right? So you the the S minus the

    likelihood ratio times the log of the likelihood ratio times the log of the likelihood
    ratio times the log of the

    your S. Um so because you have a log your S. Um so because you have a log your
    S. Um so because you have a log

    here, right? So everything needs to be here, right? So everything needs to be
    here, right? So everything needs to be

    positive now, right? And because you''re positive now, right? And because you''re
    positive now, right? And because you''re

    in a log form, so you also kind of deal in a log form, so you also kind of deal
    in a log form, so you also kind of deal

    with the crazy crazy ratio better, a with the crazy crazy ratio better, a with
    the crazy crazy ratio better, a

    little bit better. Uh and then also like little bit better. Uh and then also like
    little bit better. Uh and then also like

    now this is a KL divergence right rather now this is a KL divergence right rather
    now this is a KL divergence right rather

    than just a L2 loss right so it''s like than just a L2 loss right so it''s like
    than just a L2 loss right so it''s like

    distributionally it''s better distributionally it''s better distributionally it''s
    better

    >> what does the notation Y sim X mean in >> what does the notation Y sim X mean
    in >> what does the notation Y sim X mean in

    the the

    >> oh this is like jumping from X to Y yeah >> oh this is like jumping from X
    to Y yeah >> oh this is like jumping from X to Y yeah

    okay okay okay

    question okay anyway point being we can also okay anyway point being we can also

    apply the same reparameterization trick apply the same reparameterization trick
    apply the same reparameterization trick

    here right it''s the same thing um So here right it''s the same thing um So here
    right it''s the same thing um So

    this is how you solve the how to this is how you solve the how to this is how
    you solve the how to

    calculate the ground truth by literally calculate the ground truth by literally'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 46
  start_sec: 2592.24
  end_sec: 2680.72
  text: 'calculate the ground truth by literally

    the same trick the den noising score the same trick the den noising score the
    same trick the den noising score

    matching. This is just the noising score matching. This is just the noising score
    matching. This is just the noising score

    entropy I guess right. Um so essentially entropy I guess right. Um so essentially
    entropy I guess right. Um so essentially

    what you can do is you can uh yeah what you can do is you can uh yeah what you
    can do is you can uh yeah

    basically just uh just sample a data and basically just uh just sample a data
    and basically just uh just sample a data and

    then sample a perturb the data and and then sample a perturb the data and and
    then sample a perturb the data and and

    and then calculate the likelihood and then calculate the likelihood and then calculate
    the likelihood

    based on the the perturb uh rate that we based on the the perturb uh rate that
    we based on the the perturb uh rate that we

    have. set in in our model assumption have. set in in our model assumption have.
    set in in our model assumption

    essentially. essentially. essentially.

    All right, any questions? But anyway, if All right, any questions? But anyway,
    if All right, any questions? But anyway, if

    you don''t have questions, now you have you don''t have questions, now you have
    you don''t have questions, now you have

    the score entropy discrete diffusion the score entropy discrete diffusion the
    score entropy discrete diffusion

    sde. sde. sde.

    Okay, Okay, Okay,

    these things are confusing. Um, any these things are confusing. Um, any these
    things are confusing. Um, any

    questions about SE DD? Yeah.

    >> How do you generate from this >> How do you generate from this >> How do you
    generate from this

    train? uh basically you the uh basically you the

    hold on hold on. hold on hold on. hold on hold on.

    Okay. Oh yeah. Okay. Oh yeah. Okay. Oh yeah.

    Give me a second. All right. So, this is Give me a second. All right. So, this
    is Give me a second. All right. So, this is

    the reverse rate, right? So, you just the reverse rate, right? So, you just'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 47
  start_sec: 2680.72
  end_sec: 2739.2
  text: 'the reverse rate, right? So, you just

    replace this concrete score with the replace this concrete score with the replace
    this concrete score with the

    concrete score that you trained. And concrete score that you trained. And concrete
    score that you trained. And

    then this is the then you apply the then this is the then you apply the then this
    is the then you apply the

    rate. rate. rate.

    Yeah. Make sense? Make sense?

    Okay. Cool. Okay. Cool. Okay. Cool.

    All right. All right.

    Cool. All right. So we get to the score Cool. All right. So we get to the score
    Cool. All right. So we get to the score

    matching the score matching uh version matching the score matching uh version
    matching the score matching uh version

    of the discrete diffusion. Very nice. of the discrete diffusion. Very nice. of
    the discrete diffusion. Very nice.

    Very nice. H Very nice. H Very nice. H

    uh we''re going to talk about the the the uh we''re going to talk about the the
    the uh we''re going to talk about the the the

    flow matching version next class. The flow matching version next class. The flow
    matching version next class. The

    class is not over. Uh notice how now all class is not over. Uh notice how now
    all class is not over. Uh notice how now all

    our models are pretty generic, right? In our models are pretty generic, right?
    In our models are pretty generic, right? In

    terms of like the Q''s and stuff. This Q terms of like the Q''s and stuff. This
    Q terms of like the Q''s and stuff. This Q

    can be any Q essentially, right? But can be any Q essentially, right? But can
    be any Q essentially, right? But

    like many people have uh mentioned like many people have uh mentioned like many
    people have uh mentioned

    that you know like you can choose that you know like you can choose that you know
    like you can choose

    different cues uh and in fact many of different cues uh and in fact many of different
    cues uh and in fact many of

    you have chosen different cues you have chosen different cues you have chosen
    different cues

    >> earlier how are we choosing why do we >> earlier how are we choosing why do
    we'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 48
  start_sec: 2739.2
  end_sec: 2798.56
  text: '>> earlier how are we choosing why do we

    just randomly sample any token choices just randomly sample any token choices
    just randomly sample any token choices

    >> yeah based on >> yeah based on >> yeah based on

    >> okay so but notice how this kind of >> okay so but notice how this kind of
    >> okay so but notice how this kind of

    related I guess um so what is the related I guess um so what is the related I
    guess um so what is the

    easiest uh you know transition that we easiest uh you know transition that we
    easiest uh you know transition that we

    can have here what is the easiest can have here what is the easiest can have here
    what is the easiest

    easiest transition matrix that we can easiest transition matrix that we can easiest
    transition matrix that we can

    define or what is the easiest way to add define or what is the easiest way to
    add define or what is the easiest way to add

    noise besides you know randomly picking noise besides you know randomly picking
    noise besides you know randomly picking

    one that is called uniform or something. one that is called uniform or something.
    one that is called uniform or something.

    Yeah. Yeah.

    And what is or maybe like what is the And what is or maybe like what is the And
    what is or maybe like what is the

    one that is closest to LM one that is closest to LM one that is closest to LM

    and some of you have already mentioned and some of you have already mentioned
    and some of you have already mentioned

    it. No way. like it''s literally in the Yeah. No way. like it''s literally in
    the Yeah.

    >> Yeah. Right. It''s just random asking >> Yeah. Right. It''s just random asking
    >> Yeah. Right. It''s just random asking

    literally it''s just so easy. Um so in a literally it''s just so easy. Um so in
    a literally it''s just so easy. Um so in a

    in a graph in a graphical way. So in a graph in a graphical way. So in a graph
    in a graphical way. So

    basically like how about we can only do basically like how about we can only do'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 49
  start_sec: 2798.56
  end_sec: 2840.64
  text: 'basically like how about we can only do

    masking and unmasking, right? So in the masking and unmasking, right? So in the
    masking and unmasking, right? So in the

    forward process all you can do is you forward process all you can do is you forward
    process all you can do is you

    can you can turn an existing tokens into can you can turn an existing tokens into
    can you can turn an existing tokens into

    a mask. You cannot unmask it. Like the a mask. You cannot unmask it. Like the
    a mask. You cannot unmask it. Like the

    all you can do like if you if you all you can do like if you if you all you can
    do like if you if you

    already mask it, you cannot unmask it in already mask it, you cannot unmask it
    in already mask it, you cannot unmask it in

    in in the forward process. And then the in in the forward process. And then the
    in in the forward process. And then the

    reverse process is the opposite, right? reverse process is the opposite, right?
    reverse process is the opposite, right?

    So like you try to unmask something and So like you try to unmask something and
    So like you try to unmask something and

    then you you will not like you know then you you will not like you know then you
    you will not like you know

    remask it if you if you have already remask it if you if you have already remask
    it if you if you have already

    unmasked it. So literally this is how unmasked it. So literally this is how unmasked
    it. So literally this is how

    you do uh you know just just add random you do uh you know just just add random
    you do uh you know just just add random

    masking to each um token. And the masking to each um token. And the masking to
    each um token. And the

    transition matrix is also super simple, transition matrix is also super simple,
    transition matrix is also super simple,

    right? So essentially what you do is right? So essentially what you do is right?
    So essentially what you do is

    like basically the only two columns that like basically the only two columns that'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 50
  start_sec: 2840.64
  end_sec: 2886.88
  text: 'like basically the only two columns that

    you''re going to have non- negative value you''re going to have non- negative
    value you''re going to have non- negative value

    is the columns on the diagonal and the is the columns on the diagonal and the
    is the columns on the diagonal and the

    last column which uh like kind of last column which uh like kind of last column
    which uh like kind of

    represents the the the the transition represents the the the the transition represents
    the the the the transition

    rate to the to the to the masks. Right? rate to the to the to the masks. Right?
    rate to the to the to the masks. Right?

    So in the diagonal it represents the So in the diagonal it represents the So in
    the diagonal it represents the

    rate to stay unmasked and this is this rate to stay unmasked and this is this
    rate to stay unmasked and this is this

    is the forward transition by the way. is the forward transition by the way. is
    the forward transition by the way.

    And then and in the last column it And then and in the last column it And then
    and in the last column it

    represents the transition rate to mask. represents the transition rate to mask.
    represents the transition rate to mask.

    So just like the rate to mass the token. So just like the rate to mass the token.
    So just like the rate to mass the token.

    Okay. Okay. Okay.

    Yeah. Yeah.

    >> So in normal diffusion >> So in normal diffusion >> So in normal diffusion

    >> if we let it go for a long while and we >> if we let it go for a long while
    and we >> if we let it go for a long while and we

    have absolute uninformative blockchain have absolute uninformative blockchain
    have absolute uninformative blockchain

    noise but that''s still samples from a noise but that''s still samples from a
    noise but that''s still samples from a

    distribution. So we have different distribution. So we have different distribution.
    So we have different

    starting points to go reverse. starting points to go reverse. starting points
    to go reverse.

    >> But if we go all the way end of the day >> But if we go all the way end of
    the day'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 51
  start_sec: 2886.88
  end_sec: 2935.04
  text: '>> But if we go all the way end of the day

    everything will be masked. everything will be masked. everything will be masked.

    >> Yeah. And it''s still a distribution >> Yeah. And it''s still a distribution
    >> Yeah. And it''s still a distribution

    right? It''s a point mask. So we always right? It''s a point mask. So we always
    right? It''s a point mask. So we always

    go if you start reverse from that we go if you start reverse from that we go if
    you start reverse from that we

    >> always go to a point mass distribution >> always go to a point mass distribution
    >> always go to a point mass distribution

    where nothing has support but the all where nothing has support but the all where
    nothing has support but the all

    mask tokens. Yeah. Yeah. Good question. mask tokens. Yeah. Yeah. Good question.
    mask tokens. Yeah. Yeah. Good question.

    >> Yeah. >> Yeah.

    >> With this matrix mass tokens would just >> With this matrix mass tokens would
    just >> With this matrix mass tokens would just

    stay mass tokens with the probability of stay mass tokens with the probability
    of stay mass tokens with the probability of

    one. one. one.

    >> Uh yes >> Uh yes >> Uh yes

    >> because it''s a because like I said right >> because it''s a because like I
    said right >> because it''s a because like I said right

    if you already masked it you should not if you already masked it you should not
    if you already masked it you should not

    unmask it. Yeah. In the forward process unmask it. Yeah. In the forward process
    unmask it. Yeah. In the forward process

    only. This is a forward process. only. This is a forward process. only. This is
    a forward process.

    All right, any other questions? All right, any other questions? All right, any
    other questions?

    Okay, cool. But basically what''s Okay, cool. But basically what''s Okay, cool.
    But basically what''s

    happening is that now we actually don''t happening is that now we actually don''t
    happening is that now we actually don''t

    even need to consider all the matrix even need to consider all the matrix even
    need to consider all the matrix

    multiplication and stuff anymore. Uh multiplication and stuff anymore. Uh'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 52
  start_sec: 2935.04
  end_sec: 2991.68
  text: 'multiplication and stuff anymore. Uh

    because we simplified everything, right? because we simplified everything, right?
    because we simplified everything, right?

    So basically what what we''re essentially So basically what what we''re essentially
    So basically what what we''re essentially

    doing is literally right, we''re actually doing is literally right, we''re actually
    doing is literally right, we''re actually

    just interpolating right between a clean just interpolating right between a clean
    just interpolating right between a clean

    data and all mass data, right? and all data and all mass data, right? and all
    data and all mass data, right? and all

    mass vector. Um, so what you can do is mass vector. Um, so what you can do is
    mass vector. Um, so what you can do is

    we can literally just formulate it in we can literally just formulate it in we
    can literally just formulate it in

    this way, right? So your it is is this way, right? So your it is is this way,
    right? So your it is is

    literally just a linear interpolation or literally just a linear interpolation
    or literally just a linear interpolation or

    like basically a scheduled interpolation like basically a scheduled interpolation
    like basically a scheduled interpolation

    I guess uh between your data and or I guess uh between your data and or I guess
    uh between your data and or

    mask. So you can literally simply mask. So you can literally simply mask. So you
    can literally simply

    describe your forward function like this describe your forward function like this
    describe your forward function like this

    or you can write it as you know in a or you can write it as you know in a or you
    can write it as you know in a

    clearer form. Basically, it''s like with clearer form. Basically, it''s like with
    clearer form. Basically, it''s like with

    uh alpha t you know with alpha t um uh alpha t you know with alpha t um uh alpha
    t you know with alpha t um

    like basically one forward jump is like like basically one forward jump is like
    like basically one forward jump is like

    with alpha t probability you''re going to with alpha t probability you''re going
    to with alpha t probability you''re going to

    stay unmasked and then with one minus stay unmasked and then with one minus'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 53
  start_sec: 2991.68
  end_sec: 3068.319
  text: 'stay unmasked and then with one minus

    alpha t uh probability you''re going to alpha t uh probability you''re going to
    alpha t uh probability you''re going to

    stay masked and uh basically if we if stay masked and uh basically if we if stay
    masked and uh basically if we if

    you do it this way um then like the one you do it this way um then like the one
    you do it this way um then like the one

    step like the one small step um four can step like the one small step um four
    can step like the one small step um four can

    also be you know represented in a very also be you know represented in a very
    also be you know represented in a very

    very nice and simple form. And specifically, if you were already And specifically,
    if you were already

    get masked in the previous time step, get masked in the previous time step, get
    masked in the previous time step,

    you always stay masked. So that''s why you always stay masked. So that''s why
    you always stay masked. So that''s why

    this is one No question. All right, let''s move on. No question. All right, let''s
    move on.

    Um, Um, Um,

    so, uh, why why is this a nice thing? so, uh, why why is this a nice thing? so,
    uh, why why is this a nice thing?

    Because remember how previously when we Because remember how previously when we
    Because remember how previously when we

    were trying to do the whole elbow thing were trying to do the whole elbow thing
    were trying to do the whole elbow thing

    and then we had this like full like and then we had this like full like and then
    we had this like full like

    multip matrix multiplication like multip matrix multiplication like multip matrix
    multiplication like

    different things happening in the D3 PM different things happening in the D3 PM
    different things happening in the D3 PM

    thing. Now this very complicated thing thing. Now this very complicated thing
    thing. Now this very complicated thing

    becomes super simple. uh literally right becomes super simple. uh literally right
    becomes super simple. uh literally right

    when uh xt equals x0 and x t minus one when uh xt equals x0 and x t minus one'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 54
  start_sec: 3068.319
  end_sec: 3122.0
  text: 'when uh xt equals x0 and x t minus one

    also equals x zero um like basically if also equals x zero um like basically if
    also equals x zero um like basically if

    if you have not been masked uh at time t if you have not been masked uh at time
    t if you have not been masked uh at time t

    then you also should not have been then you also should not have been then you
    also should not have been

    masked in xt minus one. So this thing masked in xt minus one. So this thing masked
    in xt minus one. So this thing

    has probability one and like everything has probability one and like everything
    has probability one and like everything

    else have probability zero, right? But else have probability zero, right? But
    else have probability zero, right? But

    if you''re if you''re already masked at if you''re if you''re already masked at
    if you''re if you''re already masked at

    time t, then there are two options for time t, then there are two options for
    time t, then there are two options for

    you to go, right? One is that you got you to go, right? One is that you got you
    to go, right? One is that you got

    masked at this particular time step or masked at this particular time step or
    masked at this particular time step or

    you got masked before like in in the you got masked before like in in the you
    got masked before like in in the

    history, right? So basically here is history, right? So basically here is history,
    right? So basically here is

    what we''re saying that okay we''re only what we''re saying that okay we''re only
    what we''re saying that okay we''re only

    getting masked at time t. So what is the getting masked at time t. So what is
    the getting masked at time t. So what is the

    probability of that? Then that probability of that? Then that probability of that?
    Then that

    probability if you just like plug probability if you just like plug probability
    if you just like plug

    everything in then it actually gets everything in then it actually gets everything
    in then it actually gets

    simplified into this really really simplified into this really really'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 55
  start_sec: 3122.0
  end_sec: 3191.2
  text: 'simplified into this really really

    simple uh ratio. And similarly simple uh ratio. And similarly simple uh ratio.
    And similarly

    because the only other option for you is because the only other option for you
    is because the only other option for you is

    that the this basically the only opt that the this basically the only opt that
    the this basically the only opt

    other option for uh the the only other other option for uh the the only other
    other option for uh the the only other

    valid choice for the values for xt minus valid choice for the values for xt minus
    valid choice for the values for xt minus

    one will be a mask token. So just one will be a mask token. So just one will be
    a mask token. So just

    literally one minus the ratio that you literally one minus the ratio that you
    literally one minus the ratio that you

    just calculated which can be simplified just calculated which can be simplified
    just calculated which can be simplified

    into another nice ratio. All right. But anyway, um so if we sum All right. But
    anyway, um so if we sum

    everything up, then you can actually everything up, then you can actually everything
    up, then you can actually

    represent this supposedly super represent this supposedly super represent this
    supposedly super

    complicated, you know, um distribution complicated, you know, um distribution
    complicated, you know, um distribution

    where it it has a lot of m matrix where it it has a lot of m matrix where it it
    has a lot of m matrix

    multiplication into this like super multiplication into this like super multiplication
    into this like super

    super super simple form, right? So you super super simple form, right? So you
    super super simple form, right? So you

    really really only have three cases. One really really only have three cases.
    One really really only have three cases. One

    is if XT hasn''t been masked, XT minus is if XT hasn''t been masked, XT minus
    is if XT hasn''t been masked, XT minus

    one also you should just like take it one also you should just like take it one
    also you should just like take it

    over. You should you should have the over. You should you should have the'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 56
  start_sec: 3191.2
  end_sec: 3263.43
  text: 'over. You should you should have the

    same value because it hasn''t been same value because it hasn''t been same value
    because it hasn''t been

    masked. And if XT is masked, then you masked. And if XT is masked, then you masked.
    And if XT is masked, then you

    have two cases. One is that you at at have two cases. One is that you at at have
    two cases. One is that you at at

    time Xt minus one you already masked. time Xt minus one you already masked. time
    Xt minus one you already masked.

    The other case is that uh at time t The other case is that uh at time t The other
    case is that uh at time t

    minus one you haven''t been masked and minus one you haven''t been masked and
    minus one you haven''t been masked and

    you only get masked recently. So each you only get masked recently. So each you
    only get masked recently. So each

    will has this nice ratio as your will has this nice ratio as your will has this
    nice ratio as your

    probability. probability. probability.

    Okay. >> great question because we''re gonna like >> great question because we''re
    gonna like

    basically uh you know because we can basically uh you know because we can basically
    uh you know because we can

    again uh like obviously you you this is again uh like obviously you you this is
    again uh like obviously you you this is

    still your your um your objective, still your your um your objective, still your
    your um your objective,

    right? We''re dealing with the same right? We''re dealing with the same right?
    We''re dealing with the same

    elbow. So but this thing can again be elbow. So but this thing can again be elbow.
    So but this thing can again be

    reparameterized into this thing times uh reparameterized into this thing times
    uh reparameterized into this thing times uh

    you know uh the the clean uh h you know uh the the clean uh h you know uh the
    the clean uh h

    prediction. So literally your prediction prediction. So literally your prediction
    prediction. So literally your prediction

    is literally just going to be a ratio is literally just going to be a ratio is
    literally just going to be a ratio

    times the clean data estimation.'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 57
  start_sec: 3263.43
  end_sec: 3326.559
  text: 'times the clean data estimation. times the clean data estimation.

    That''s it. >> We have that problem because we''ll start >> We have that problem
    because we''ll start

    with full mask. So if you start with with full mask. So if you start with with
    full mask. So if you start with

    full mass, we can only ever end up in full mass, we can only ever end up in full
    mass, we can only ever end up in

    one possible x0. one possible x0. one possible x0.

    >> Uh but this is for every token position. >> Uh but this is for every token
    position. >> Uh but this is for every token position.

    So for every token position, you you So for every token position, you you So for
    every token position, you you

    sort of independently mask sort of independently mask sort of independently mask

    >> it will end up being full mask, right? >> it will end up being full mask, right?
    >> it will end up being full mask, right?

    Because every token Because every token Because every token

    >> yeah eventually end up being full mask >> yeah eventually end up being full
    mask >> yeah eventually end up being full mask

    and then in reverse time you just apply and then in reverse time you just apply
    and then in reverse time you just apply

    this transition essentially every single this transition essentially every single
    this transition essentially every single

    step at each token. So like when you are step at each token. So like when you
    are step at each token. So like when you are

    unmasked already you don''t change it. If unmasked already you don''t change it.
    If unmasked already you don''t change it. If

    you if you haven''t been unmasked then you if you haven''t been unmasked then
    you if you haven''t been unmasked then

    you decide whether to unmask it in the you decide whether to unmask it in the
    you decide whether to unmask it in the

    next time step with this probability or next time step with this probability or
    next time step with this probability or

    not. >> The starting reverse is full mask. >> The starting reverse is full mask.

    >> Yeah. >> Yeah.

    >> So you''re always starting with the full >> So you''re always starting with
    the full'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 58
  start_sec: 3326.559
  end_sec: 3372.799
  text: '>> So you''re always starting with the full

    mask. mask. mask.

    >> That''s right. >> That''s right. >> That''s right.

    >> So if that one reverse gets you to I >> So if that one reverse gets you to
    I >> So if that one reverse gets you to I

    love cat. What possibility is for you to love cat. What possibility is for you
    to love cat. What possibility is for you to

    read some other thing? But this okay th read some other thing? But this okay th
    read some other thing? But this okay th

    this this thing is so stochastic right this this thing is so stochastic right
    this this thing is so stochastic right

    this whole thing is so stocastic this whole thing is so stocastic this whole thing
    is so stocastic

    like basically this is a categorical like basically this is a categorical like
    basically this is a categorical

    distribution and then you sample from distribution and then you sample from distribution
    and then you sample from

    the categorical distribution. the categorical distribution. the categorical distribution.

    >> Yeah. Okay. Yeah. >> Yeah. Okay. Yeah. >> Yeah. Okay. Yeah.

    >> Uh is there also something do we also >> Uh is there also something do we also
    >> Uh is there also something do we also

    like remask stuff? like remask stuff? like remask stuff?

    >> No you don''t you never remask >> No you don''t you never remask >> No you
    don''t you never remask

    related to this question. What if the related to this question. What if the related
    to this question. What if the

    model wants to change some word after it model wants to change some word after
    it model wants to change some word after it

    is generated when it generates is generated when it generates is generated when
    it generates

    something? in this case. Yeah. But in something? in this case. Yeah. But in something?
    in this case. Yeah. But in

    the other case, in the in in the uniform the other case, in the in in the uniform
    the other case, in the in in the uniform

    case, it does, right? Yeah. Which is why case, it does, right? Yeah. Which is
    why case, it does, right? Yeah. Which is why

    actually a good point. Basically, uh the actually a good point. Basically, uh
    the'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 59
  start_sec: 3372.799
  end_sec: 3429.599
  text: 'actually a good point. Basically, uh the

    the the mercury um founder, Inception the the mercury um founder, Inception the
    the mercury um founder, Inception

    Lab founder, Stephano, who is the one of Lab founder, Stephano, who is the one
    of Lab founder, Stephano, who is the one of

    the inventors of diffusion models. He the inventors of diffusion models. He the
    inventors of diffusion models. He

    said that in in on his website, I guess, said that in in on his website, I guess,
    said that in in on his website, I guess,

    that like a diffusion language model can that like a diffusion language model
    can that like a diffusion language model can

    correct its own uh hallucination correct its own uh hallucination correct its
    own uh hallucination

    is only true because they were using the is only true because they were using
    the is only true because they were using the

    uniform thing. uniform thing. uniform thing.

    >> Yeah, >> Yeah, >> Yeah,

    they''re probably not using the mass they''re probably not using the mass they''re
    probably not using the mass

    thing. Well, I don''t know now, but at thing. Well, I don''t know now, but at
    thing. Well, I don''t know now, but at

    the time that he claimed this, they were the time that he claimed this, they were
    the time that he claimed this, they were

    using the uniform thing. Oh, by the way, using the uniform thing. Oh, by the way,
    using the uniform thing. Oh, by the way,

    the SD thing is also from Stephano. So, the SD thing is also from Stephano. So,
    the SD thing is also from Stephano. So,

    yeah. Well, like this this categorical you''re Well, like this this categorical
    you''re

    sampling from a categorical distribution sampling from a categorical distribution
    sampling from a categorical distribution

    stoastically. stoastically. stoastically.

    Yeah. For each token. Yeah. For each token. Yeah. For each token.

    Okay. Uh but anyway, uh the objective Okay. Uh but anyway, uh the objective Okay.
    Uh but anyway, uh the objective

    function is actually surprisingly easy function is actually surprisingly easy
    function is actually surprisingly easy

    because basically what you do is you you because basically what you do is you
    you because basically what you do is you you

    you can also do like continuous time you can also do like continuous time'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 60
  start_sec: 3429.599
  end_sec: 3478.16
  text: 'you can also do like continuous time

    training with this. You literally just training with this. You literally just
    training with this. You literally just

    take the continuous time limit of the of take the continuous time limit of the
    of take the continuous time limit of the of

    this ratio here and then this thing this ratio here and then this thing this ratio
    here and then this thing

    happened to just be this right. It''s happened to just be this right. It''s happened
    to just be this right. It''s

    super easy. And then this thing is just super easy. And then this thing is just
    super easy. And then this thing is just

    cross entropy between the clean data and cross entropy between the clean data
    and cross entropy between the clean data and

    the and your estimation is like bird the and your estimation is like bird the
    and your estimation is like bird

    basically. So is low key just a uh way basically. So is low key just a uh way
    basically. So is low key just a uh way

    to burn to burn to burn

    zooming out a little bit but I thought zooming out a little bit but I thought
    zooming out a little bit but I thought

    the whole point so in this objective the whole point so in this objective the
    whole point so in this objective

    we''re still sampling one token at a time we''re still sampling one token at a
    time we''re still sampling one token at a time

    but I thought that but I thought that but I thought that

    >> well you can parallely sample all tokens >> well you can parallely sample all
    tokens >> well you can parallely sample all tokens

    right so like all of these all of the right so like all of these all of the right
    so like all of these all of the

    categorical sampling happens categorical sampling happens categorical sampling
    happens

    independently at each token location independently at each token location independently
    at each token location

    >> the number of tokens we sample >> the number of tokens we sample >> the number
    of tokens we sample

    >> uh you yes kind of so it''s the same >> uh you yes kind of so it''s the same'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 61
  start_sec: 3478.16
  end_sec: 3522.549
  text: '>> uh you yes kind of so it''s the same

    thing it''s uh like analogy to you choose thing it''s uh like analogy to you choose
    thing it''s uh like analogy to you choose

    the number of sampling steps right in the number of sampling steps right in the
    number of sampling steps right in

    continuous diffusion. So here you also continuous diffusion. So here you also
    continuous diffusion. So here you also

    kind of like you you you kind you also kind of like you you you kind you also
    kind of like you you you kind you also

    choose the number of time steps kind of choose the number of time steps kind of
    choose the number of time steps kind of

    and then basically depending on the and then basically depending on the and then
    basically depending on the

    number of time steps um like you just number of time steps um like you just number
    of time steps um like you just

    like you don''t really choose the like like you don''t really choose the like
    like you don''t really choose the like

    the number of unmasking to tokens that the number of unmasking to tokens that
    the number of unmasking to tokens that

    you have at each step but what you do is you have at each step but what you do
    is you have at each step but what you do is

    you basically adjust your scheduleuler you basically adjust your scheduleuler
    you basically adjust your scheduleuler

    based on the current step that you add based on the current step that you add
    based on the current step that you add

    and then you sample via the categorical and then you sample via the categorical
    and then you sample via the categorical

    distribution and if the categorical distribution and if the categorical distribution
    and if the categorical

    distribution give you I''m mass token distribution give you I''m mass token distribution
    give you I''m mass token

    there you are. Uh but if they decided to there you are. Uh but if they decided
    to there you are. Uh but if they decided to

    stay mass then they will stay mass but stay mass then they will stay mass but
    stay mass then they will stay mass but

    this is purely depending on like the the'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 62
  start_sec: 3522.549
  end_sec: 3574.24
  text: 'this is purely depending on like the the this is purely depending on like
    the the

    model that you got trained but usually model that you got trained but usually
    model that you got trained but usually

    if you are trying to sample with smaller if you are trying to sample with smaller
    if you are trying to sample with smaller

    time steps then it will try to basically time steps then it will try to basically
    time steps then it will try to basically

    for each individual tokens it''ll be more for each individual tokens it''ll be
    more for each individual tokens it''ll be more

    aggressive and so it''s more likely for aggressive and so it''s more likely for
    aggressive and so it''s more likely for

    you to see like parallel multiple tokens you to see like parallel multiple tokens
    you to see like parallel multiple tokens

    get unmasked at the same time. All get unmasked at the same time. All get unmasked
    at the same time. All

    right, we I don''t think I gave you a a right, we I don''t think I gave you a
    a right, we I don''t think I gave you a a

    blessing yet. Uh, Rich, get rich. Uh, Rich, get rich.

    >> Sure. >> Sure. >> Sure.

    >> All right. Oh, this is a good good one. >> All right. Oh, this is a good good
    one. >> All right. Oh, this is a good good one.

    Okay. Anyway. All right. Any other Okay. Anyway. All right. Any other Okay. Anyway.
    All right. Any other

    questions? questions? questions?

    We don''t have any heavy math after this, We don''t have any heavy math after
    this, We don''t have any heavy math after this,

    so we can stay for a little bit longer. so we can stay for a little bit longer.
    so we can stay for a little bit longer.

    Yeah. Does the ratio change over time Yeah. Does the ratio change over time Yeah.
    Does the ratio change over time

    like or is it the same? like or is it the same? like or is it the same?

    >> Uh it change over time, right? Like >> Uh it change over time, right? Like
    >> Uh it change over time, right? Like

    basically the mask ratio is depending on basically the mask ratio is depending
    on'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 63
  start_sec: 3574.24
  end_sec: 3634.549
  text: 'basically the mask ratio is depending on

    this alpha t thing which you set. So you this alpha t thing which you set. So
    you this alpha t thing which you set. So you

    you can you can choose uh but like you you can you can choose uh but like you
    you can you can choose uh but like you

    can you can have a linear it''s the same can you can have a linear it''s the same
    can you can have a linear it''s the same

    thing as DDPM right so you can you can thing as DDPM right so you can you can
    thing as DDPM right so you can you can

    choose a linear schedule you can choose choose a linear schedule you can choose
    choose a linear schedule you can choose

    a cosine schedule you can choose a cosine schedule you can choose a cosine schedule
    you can choose

    whatever schedule you want. Yeah. Is whatever schedule you want. Yeah. Is whatever
    schedule you want. Yeah. Is

    this tied to the >> uh it like statistically? Yes. But like >> uh it like statistically?
    Yes. But like

    you don''t decide how many tokens you uh you don''t decide how many tokens you
    uh you don''t decide how many tokens you uh

    amass basically. >> Yeah. Yeah. Yeah. Yeah. Yeah. So that''s >> Yeah. Yeah. Yeah.
    Yeah. Yeah. So that''s

    why so so that''s why you have this why so so that''s why you have this why so
    so that''s why you have this

    ratio, right? Like basically um yeah ratio, right? Like basically um yeah ratio,
    right? Like basically um yeah

    here is t the number of is t the number of

    the token that we''ve generated like say the token that we''ve generated like
    say the token that we''ve generated like say

    third token in subsequ third token in subsequ third token in subsequ

    steps. Yeah. T is the diffusion time steps. Yeah. T is the diffusion time steps.
    Yeah. T is the diffusion time

    step here. Yeah. And then the the the step here. Yeah. And then the the the step
    here. Yeah. And then the the the

    the tokens are the L L''s here. L L are the tokens are the L L''s here. L L are
    the tokens are the L L''s here. L L are

    the tokens.'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 64
  start_sec: 3634.549
  end_sec: 3676.88
  text: 'the tokens. the tokens.

    >> Yeah. >> Yeah.

    >> But then in the last you have something >> But then in the last you have something
    >> But then in the last you have something

    like XT equal to M. So like XT equal to M. So like XT equal to M. So

    >> uh yeah. So that just means that Oh, >> uh yeah. So that just means that Oh,
    >> uh yeah. So that just means that Oh,

    sorry. Okay. Yeah. So everything before sorry. Okay. Yeah. So everything before
    sorry. Okay. Yeah. So everything before

    this slide XT is one token but all the this slide XT is one token but all the
    this slide XT is one token but all the

    tokens are independent. So this is why I tokens are independent. So this is why
    I tokens are independent. So this is why I

    just didn''t this why they can be added just didn''t this why they can be added
    just didn''t this why they can be added

    together which is sounds wrong right it together which is sounds wrong right it
    together which is sounds wrong right it

    just doesn''t sound right but anyway but just doesn''t sound right but anyway
    but just doesn''t sound right but anyway but

    but but yeah but we''re going to talk but but yeah but we''re going to talk but
    but yeah but we''re going to talk

    about uh about uh about uh

    how may or may not people try to solve how may or may not people try to solve
    how may or may not people try to solve

    it actually but yeah they don''t really it actually but yeah they don''t really
    it actually but yeah they don''t really

    but you know but you know but you know

    >> this output is in the token space does >> this output is in the token space
    does >> this output is in the token space does

    this mean we cannot do like a latent this mean we cannot do like a latent this
    mean we cannot do like a latent

    text decoding of diffusion models text decoding of diffusion models text decoding
    of diffusion models

    >> uh what do you mean by latent text well >> uh what do you mean by latent text
    well'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 65
  start_sec: 3676.88
  end_sec: 3722.87
  text: '>> uh what do you mean by latent text well

    like so you mean like like so you mean like like so you mean like

    a region space for images and then use a region space for images and then use
    a region space for images and then use

    like a V come back. like a V come back. like a V come back.

    >> Ah, I see. I see. >> Ah, I see. I see. >> Ah, I see. I see.

    >> That''s >> That''s >> That''s

    >> Yeah. Yeah. Right. Yeah. So basically >> Yeah. Yeah. Right. Yeah. So basically
    >> Yeah. Yeah. Right. Yeah. So basically

    you don''t you don''t really have a you don''t you don''t really have a you don''t
    you don''t really have a

    discrete. So there are too many discrete discrete. So there are too many discrete
    discrete. So there are too many discrete

    steps here I guess to have a like a VA steps here I guess to have a like a VA
    steps here I guess to have a like a VA

    style uh thing here. Yeah. Yeah. So style uh thing here. Yeah. Yeah. So style
    uh thing here. Yeah. Yeah. So

    right right now nobody is doing that. right right now nobody is doing that. right
    right now nobody is doing that.

    But may maybe it''s visible. Who knows? But may maybe it''s visible. Who knows?
    But may maybe it''s visible. Who knows?

    >> Like you have to decide what length you >> Like you have to decide what length
    you >> Like you have to decide what length you

    want to I don''t know the want to I don''t know the want to I don''t know the

    >> Yeah. Yeah. Yeah. Yeah. Yeah. The the >> Yeah. Yeah. Yeah. Yeah. Yeah. The
    the >> Yeah. Yeah. Yeah. Yeah. Yeah. The the

    the variable length here, the L thing is the variable length here, the L thing
    is the variable length here, the L thing is

    a big thing. They Yeah. This is why it''s a big thing. They Yeah. This is why
    it''s a big thing. They Yeah. This is why it''s

    kind of not very efficient the the kind of not very efficient the the kind of
    not very efficient the the

    model. model. model.

    >> Does it produce something coherent if'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 66
  start_sec: 3722.87
  end_sec: 3769.52
  text: '>> Does it produce something coherent if >> Does it produce something coherent
    if

    all the things are independently getting all the things are independently getting
    all the things are independently getting

    masked? masked? masked?

    Well, the model itself is trained in Well, the model itself is trained in Well,
    the model itself is trained in

    with like self attention from from with like self attention from from with like
    self attention from from

    everywhere, right? So, basically, it''s everywhere, right? So, basically, it''s
    everywhere, right? So, basically, it''s

    sort of like just imagine like the edge sort of like just imagine like the edge
    sort of like just imagine like the edge

    case where you only have one token case where you only have one token case where
    you only have one token

    masked, right? Then it''s very easy to to masked, right? Then it''s very easy
    to to masked, right? Then it''s very easy to to

    to to determine which token it is, to to determine which token it is, to to determine
    which token it is,

    right, based on your data distribution right, based on your data distribution
    right, based on your data distribution

    and then you can just induction. and then you can just induction. and then you
    can just induction.

    >> Yeah. >> Yeah.

    >> Assume that because you''re summing over >> Assume that because you''re summing
    over >> Assume that because you''re summing over

    all tokens, it will learn some structure all tokens, it will learn some structure
    all tokens, it will learn some structure

    between the tokens. between the tokens. between the tokens.

    >> Yeah, basically. So because you''re >> Yeah, basically. So because you''re
    >> Yeah, basically. So because you''re

    you''re dealing like all the tokens share you''re dealing like all the tokens
    share you''re dealing like all the tokens share

    the same model, they see the same thing. the same model, they see the same thing.
    the same model, they see the same thing.

    So yeah, you kind of depend on the the So yeah, you kind of depend on the the
    So yeah, you kind of depend on the the

    model. model.

    >> It''s like recursive birth basically. >> It''s like recursive birth basically.
    >> It''s like recursive birth basically.

    >> It is pretty much just birth literally >> It is pretty much just birth literally'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 67
  start_sec: 3769.52
  end_sec: 3820.48
  text: '>> It is pretty much just birth literally

    if you think about it. Yeah. if you think about it. Yeah. if you think about it.
    Yeah.

    >> Well, between like >> Well, between like >> Well, between like

    >> you call arbitrary length. I''m going to >> you call arbitrary length. I''m
    going to >> you call arbitrary length. I''m going to

    talk about it like next class, but it''s talk about it like next class, but it''s
    talk about it like next class, but it''s

    like very very hacky. Well, sorry for like very very hacky. Well, sorry for like
    very very hacky. Well, sorry for

    the people who developed the method, but the people who developed the method,
    but the people who developed the method, but

    I think it''s kind of hacky. Okay. I think it''s kind of hacky. Okay. I think
    it''s kind of hacky. Okay.

    Anyway, Anyway, Anyway,

    >> you didn''t specify any sort of >> you didn''t specify any sort of >> you didn''t
    specify any sort of

    location position. location position. location position.

    >> Oh, yeah. Yeah, they do have all the >> Oh, yeah. Yeah, they do have all the
    >> Oh, yeah. Yeah, they do have all the

    positional embeddings and everything. positional embeddings and everything. positional
    embeddings and everything.

    Yeah. Yeah.

    >> Yeah. >> Yeah.

    >> Yeah. >> Oh, no. So, this thing cannot, right? >> Oh, no. So, this thing cannot,
    right?

    But the thing that we saw before the But the thing that we saw before the But
    the thing that we saw before the

    uniform version, it can, right? Because uniform version, it can, right? Because
    uniform version, it can, right? Because

    you can sample any tokens. Even if you you can sample any tokens. Even if you
    you can sample any tokens. Even if you

    has already sampled the token, you can has already sampled the token, you can
    has already sampled the token, you can

    still sample again at this location. still sample again at this location. still
    sample again at this location.

    Right? So this is what Stephano meant Right? So this is what Stephano meant Right?
    So this is what Stephano meant

    when they when he said like oh we can when they when he said like oh we can'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 68
  start_sec: 3820.48
  end_sec: 3864.16
  text: 'when they when he said like oh we can

    correct hallucination but like here we correct hallucination but like here we
    correct hallucination but like here we

    cannot really it''s the same as cannot really it''s the same as cannot really
    it''s the same as

    >> LM how do we know when to stop? We have how do we know when to stop? We have

    like a fixed time. like a fixed time. like a fixed time.

    >> You have a fixed time step, right? So >> You have a fixed time step, right?
    So >> You have a fixed time step, right? So

    you just run it till the end. you just run it till the end. you just run it till
    the end.

    >> Okay. Uh we have like one more minute. >> Okay. Uh we have like one more minute.
    >> Okay. Uh we have like one more minute.

    So but yeah, now you have mass diffusion So but yeah, now you have mass diffusion
    So but yeah, now you have mass diffusion

    model. Hey. All right. So we uh let''s go model. Hey. All right. So we uh let''s
    go model. Hey. All right. So we uh let''s go

    through the last thing. Uh so basically through the last thing. Uh so basically
    through the last thing. Uh so basically

    it works super well and also like it works super well and also like it works super
    well and also like

    uh very coincidentally I feel like this uh very coincidentally I feel like this
    uh very coincidentally I feel like this

    is happening more and more in the age of is happening more and more in the age
    of is happening more and more in the age of

    gender modeling unfortunately. Oh I gender modeling unfortunately. Oh I gender
    modeling unfortunately. Oh I

    don''t know if it''s unfortunate fortunate don''t know if it''s unfortunate fortunate
    don''t know if it''s unfortunate fortunate

    like if you''re outside of the drama like if you''re outside of the drama like
    if you''re outside of the drama

    you''re you you feel really nice. This is you''re you you feel really nice. This
    is you''re you you feel really nice. This is

    like a sort of like a like a like a like like a sort of like a like a like a like'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 69
  start_sec: 3864.16
  end_sec: 3908.559
  text: 'like a sort of like a like a like a like

    a interesting moment in science. But if a interesting moment in science. But if
    a interesting moment in science. But if

    you''re one of the authors, you may get, you''re one of the authors, you may get,
    you''re one of the authors, you may get,

    you know, you may be like what what what you know, you may be like what what what
    you know, you may be like what what what

    am I what is going on? But anyway, uh am I what is going on? But anyway, uh am
    I what is going on? But anyway, uh

    but they kind of like the math diffusion but they kind of like the math diffusion
    but they kind of like the math diffusion

    formulation like literally pretty much formulation like literally pretty much
    formulation like literally pretty much

    the same uh like loss function was the same uh like loss function was the same
    uh like loss function was

    discovered by two concurrent work at new discovered by two concurrent work at
    new discovered by two concurrent work at new

    rips uh 2024. Literally they''re even rips uh 2024. Literally they''re even rips
    uh 2024. Literally they''re even

    even their titles are kind of similar even their titles are kind of similar even
    their titles are kind of similar

    honestly. So it just uh but but yeah but honestly. So it just uh but but yeah
    but honestly. So it just uh but but yeah but

    they are concurrent. So they they they they are concurrent. So they they they
    they are concurrent. So they they they

    both discovered it um you know both discovered it um you know both discovered
    it um you know

    independently. So this is just shows how independently. So this is just shows
    how independently. So this is just shows how

    this is a super effective um like method this is a super effective um like method
    this is a super effective um like method

    essentially. Yeah. essentially. Yeah. essentially. Yeah.

    >> Both papers were written by AI >> Both papers were written by AI >> Both papers
    were written by AI

    >> very low because it''s 2024. Okay. Anyway >> very low because it''s 2024. Okay.
    Anyway'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 70
  start_sec: 3908.559
  end_sec: 3955.67
  text: '>> very low because it''s 2024. Okay. Anyway

    um but since like you know people show um but since like you know people show
    um but since like you know people show

    saw the potential of this they have saw the potential of this they have saw the
    potential of this they have

    actually tried to scale it up. Uh so actually tried to scale it up. Uh so actually
    tried to scale it up. Uh so

    there this thing called lada uh which is there this thing called lada uh which
    is there this thing called lada uh which is

    basically try to scale up in an LM scale basically try to scale up in an LM scale
    basically try to scale up in an LM scale

    and try to do like instruction and try to do like instruction and try to do like
    instruction

    fine-tunings and everything like that fine-tunings and everything like that fine-tunings
    and everything like that

    and the loss function they use basically and the loss function they use basically
    and the loss function they use basically

    they just like have like a very specific they just like have like a very specific
    they just like have like a very specific

    uh you know uh noise scheduling and then uh you know uh noise scheduling and then
    uh you know uh noise scheduling and then

    basically the the the the ratio that we basically the the the the ratio that we
    basically the the the the ratio that we

    saw at the beginning uh in the last saw at the beginning uh in the last saw at
    the beginning uh in the last

    slides reduce to one over t. So it''s slides reduce to one over t. So it''s slides
    reduce to one over t. So it''s

    literally just 1 / t times cross entropy literally just 1 / t times cross entropy
    literally just 1 / t times cross entropy

    at places where you have masks. at places where you have masks. at places where
    you have masks.

    That''s it. Like super super super easy. That''s it. Like super super super easy.
    That''s it. Like super super super easy.

    Um but it works pretty well. Let''s just Um but it works pretty well. Let''s just
    Um but it works pretty well. Let''s just

    say and seems like super compatible uh'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 71
  start_sec: 3955.67
  end_sec: 3999.28
  text: 'say and seems like super compatible uh say and seems like super compatible
    uh

    to comparable to like large language to comparable to like large language to comparable
    to like large language

    models like llama. So it''s like super models like llama. So it''s like super
    models like llama. So it''s like super

    nice. Um yeah but anyway uh so we have nice. Um yeah but anyway uh so we have
    nice. Um yeah but anyway uh so we have

    talked about two formulations for talked about two formulations for talked about
    two formulations for

    discrete diffusion. uh the next class discrete diffusion. uh the next class discrete
    diffusion. uh the next class

    we''re going to talk about essentially we''re going to talk about essentially
    we''re going to talk about essentially

    the flow matching equivalence of uh the flow matching equivalence of uh the flow
    matching equivalence of uh

    discrete diffusion and it''s actually a discrete diffusion and it''s actually
    a discrete diffusion and it''s actually a

    very very interesting recent work about very very interesting recent work about
    very very interesting recent work about

    that and uh lastly this is like a very that and uh lastly this is like a very
    that and uh lastly this is like a very

    very big trend right now essentially very big trend right now essentially very
    big trend right now essentially

    like people are trying to connect LMS like people are trying to connect LMS like
    people are trying to connect LMS

    with uh with uh with uh

    um discrete diffusion and uh yeah let''s um discrete diffusion and uh yeah let''s
    um discrete diffusion and uh yeah let''s

    just like kind of like look at some of just like kind of like look at some of
    just like kind of like look at some of

    the efforts that people have put in it the efforts that people have put in it
    the efforts that people have put in it

    yeah but that''s it yeah thanks for yeah but that''s it yeah thanks for yeah but
    that''s it yeah thanks for

    coming uh yeah if you guys want snacks coming uh yeah if you guys want snacks
    coming uh yeah if you guys want snacks

    Please come up and uh can get rich as Please come up and uh can get rich as'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
- idx: 72
  start_sec: 3999.28
  end_sec: 4004.599
  text: 'Please come up and uh can get rich as

    well. All right, see you guys next well. All right, see you guys next well. All
    right, see you guys next

    class.'
  concept_slugs:
  - discrete-diffusion
  - masked-diffusion
  - score-entropy-discrete-diffusion
---
# CMU 10799 S26: Lecture 12 - Discrete Diffusion & Masked Diffusion - Diffusion & Flow Matching

See the structured chunks above.
