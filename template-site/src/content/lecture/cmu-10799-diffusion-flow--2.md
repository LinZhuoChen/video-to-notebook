---
course_slug: cmu-10799-diffusion-flow
idx: 2
title: 'CMU 10799 S26: Lecture 3 - Modal Guest Lecture - Diffusion & Flow Matching'
video_url: https://www.youtube.com/watch?v=dPVpmv4eFnM
duration_sec: null
chunks:
- idx: 0
  start_sec: 4.789
  end_sec: 48.47
  text: 'Okay, cool. All right, cool. Let''s get Okay, cool. All right, cool. Let''s
    get

    started. I''m so sorry everyone that started. I''m so sorry everyone that started.
    I''m so sorry everyone that

    we''re navigating the the modern we''re navigating the the modern we''re navigating
    the the modern

    technology here. It took a while. Can''t technology here. It took a while. Can''t
    technology here. It took a while. Can''t

    believe we''re computer science majors. believe we''re computer science majors.
    believe we''re computer science majors.

    But anyway, uh yeah, so today we''re we But anyway, uh yeah, so today we''re we
    But anyway, uh yeah, so today we''re we

    have Charles from Thank you so much. Um have Charles from Thank you so much. Um
    have Charles from Thank you so much. Um

    from model to talk about how to use from model to talk about how to use from model
    to talk about how to use

    their service. Uh so let me just share a their service. Uh so let me just share
    a their service. Uh so let me just share a

    little bit about my uh my experience. So little bit about my uh my experience.
    So little bit about my uh my experience. So

    I literally prepared everything. So all I literally prepared everything. So all
    I literally prepared everything. So all

    of your homework starter code were of your homework starter code were of your
    homework starter code were

    prepared on model. Um I only did testing prepared on model. Um I only did testing
    prepared on model. Um I only did testing

    on Babel and everything else was on on Babel and everything else was on on Babel
    and everything else was on

    model. It was amazing. It''s like really model. It was amazing. It''s like really
    model. It was amazing. It''s like really

    really easy uh to do everything. And uh really easy uh to do everything. And uh
    really easy uh to do everything. And uh

    yeah so today Charles is going to talk yeah so today Charles is going to talk
    yeah so today Charles is going to talk

    about like what you guys are going to about like what you guys are going to about
    like what you guys are going to

    do. Uh and before he started let me do. Uh and before he started let me'
  concept_slugs: []
- idx: 1
  start_sec: 48.47
  end_sec: 91.759
  text: 'do. Uh and before he started let me

    [clears throat] just like do a few quick [clears throat] just like do a few quick
    [clears throat] just like do a few quick

    uh reminder. Basically please start uh reminder. Basically please start uh reminder.
    Basically please start

    doing your homework now. It''s going to doing your homework now. It''s going to
    doing your homework now. It''s going to

    take time to train models. just try to take time to train models. just try to
    take time to train models. just try to

    start right now. And also I have a poll start right now. And also I have a poll
    start right now. And also I have a poll

    on on the discord channel basically just on on the discord channel basically just
    on on the discord channel basically just

    like uh if you guys want to make one of like uh if you guys want to make one of
    like uh if you guys want to make one of

    the more difficult question an option the more difficult question an option the
    more difficult question an option

    one so that you guys have more time to one so that you guys have more time to
    one so that you guys have more time to

    just know properly do everything. Uh if just know properly do everything. Uh if
    just know properly do everything. Uh if

    you if we get more than 35 people to you if we get more than 35 people to you
    if we get more than 35 people to

    vote yes, we''re gonna cancel that not vote yes, we''re gonna cancel that not
    vote yes, we''re gonna cancel that not

    cancel, we''re gonna make that uh cancel, we''re gonna make that uh cancel, we''re
    gonna make that uh

    question optional. Okay, cool. Uh yeah, question optional. Okay, cool. Uh yeah,
    question optional. Okay, cool. Uh yeah,

    Charles, please uh take it away from Charles, please uh take it away from Charles,
    please uh take it away from

    here. here. here.

    Yeah, thanks for the uh wonderful Yeah, thanks for the uh wonderful Yeah, thanks
    for the uh wonderful

    introduction, Kelly. Um, you know, it''s introduction, Kelly. Um, you know, it''s
    introduction, Kelly. Um, you know, it''s

    uh it''s one thing for me to say that uh it''s one thing for me to say that'
  concept_slugs: []
- idx: 2
  start_sec: 91.759
  end_sec: 132.71
  text: 'uh it''s one thing for me to say that

    modal is easy to use and uh and fun and modal is easy to use and uh and fun and
    modal is easy to use and uh and fun and

    wonderful, but you know, they pay me to wonderful, but you know, they pay me to
    wonderful, but you know, they pay me to

    say that. Uh so, you know, it''s another say that. Uh so, you know, it''s another
    say that. Uh so, you know, it''s another

    thing to hear it from uh from somebody thing to hear it from uh from somebody
    thing to hear it from uh from somebody

    like Kelly. Um and yeah, and speaking of like Kelly. Um and yeah, and speaking
    of like Kelly. Um and yeah, and speaking of

    not wanting to just hit y''all with a not wanting to just hit y''all with a not
    wanting to just hit y''all with a

    sales pitch, I actually decided uh I''m sales pitch, I actually decided uh I''m
    sales pitch, I actually decided uh I''m

    going to split the talk into kind of two going to split the talk into kind of
    two going to split the talk into kind of two

    pieces. I''m going to spend half the talk pieces. I''m going to spend half the
    talk pieces. I''m going to spend half the talk

    actually just talking about kind of like actually just talking about kind of like
    actually just talking about kind of like

    a fun image diffusion model related a fun image diffusion model related a fun
    image diffusion model related

    project that I built um Q art codes. Uh project that I built um Q art codes. Uh
    project that I built um Q art codes. Uh

    and so just like kind of share and talk and so just like kind of share and talk
    and so just like kind of share and talk

    about some like some things that you run about some like some things that you
    run about some like some things that you run

    into using you know using diffusion into using you know using diffusion into using
    you know using diffusion

    models for an actual um like application models for an actual um like application
    models for an actual um like application

    uh with some fun ML lessons along the'
  concept_slugs: []
- idx: 3
  start_sec: 132.71
  end_sec: 182.0
  text: 'uh with some fun ML lessons along the uh with some fun ML lessons along the

    way. Uh and then you know I built that way. Uh and then you know I built that
    way. Uh and then you know I built that

    project on modal the cloud platform that project on modal the cloud platform that
    project on modal the cloud platform that

    I work on. Um, and so then I''ll spend I work on. Um, and so then I''ll spend
    I work on. Um, and so then I''ll spend

    the second half sort of like talking the second half sort of like talking the
    second half sort of like talking

    about modal in particular, how to use it about modal in particular, how to use
    it about modal in particular, how to use it

    and and what it''s for and and how to how and and what it''s for and and how to
    how and and what it''s for and and how to how

    to get started as well. Um, so to start to get started as well. Um, so to start
    to get started as well. Um, so to start

    off um let''s talk about QR codes. Um so off um let''s talk about QR codes. Um
    so off um let''s talk about QR codes. Um so

    this uh for this project I tamed the uh this uh for this project I tamed the uh
    this uh for this project I tamed the uh

    these uh diffusion QR codes using some these uh diffusion QR codes using some
    these uh diffusion QR codes using some

    key techniques for for operationalizing key techniques for for operationalizing
    key techniques for for operationalizing

    ML applications eval inference time ML applications eval inference time ML applications
    eval inference time

    compute scaling. Um so kind of a fun compute scaling. Um so kind of a fun compute
    scaling. Um so kind of a fun

    little uh classic story of how to make little uh classic story of how to make
    little uh classic story of how to make

    ML better. Um so uh what you see on the ML better. Um so uh what you see on the
    ML better. Um so uh what you see on the

    screen there is a QR code, a quick screen there is a QR code, a quick'
  concept_slugs: []
- idx: 4
  start_sec: 182.0
  end_sec: 226.239
  text: 'screen there is a QR code, a quick

    response code. It stores a precise bit response code. It stores a precise bit
    response code. It stores a precise bit

    pattern in a physical image. So not the pattern in a physical image. So not the
    pattern in a physical image. So not the

    pattern of bits that make up the image pattern of bits that make up the image
    pattern of bits that make up the image

    when you represent it on a computer, but when you represent it on a computer,
    but when you represent it on a computer, but

    a much smaller pattern of bits that are a much smaller pattern of bits that are
    a much smaller pattern of bits that are

    encoded in the black and white uh like encoded in the black and white uh like
    encoded in the black and white uh like

    uh physical sort of uh patterns of light uh physical sort of uh patterns of light
    uh physical sort of uh patterns of light

    in this image. And uh the QR there in this image. And uh the QR there in this
    image. And uh the QR there

    there''s this is like a specific uh you there''s this is like a specific uh you
    there''s this is like a specific uh you

    know format. there''s QR code readers and know format. there''s QR code readers
    and know format. there''s QR code readers and

    QR code generators and they agree on how QR code generators and they agree on
    how QR code generators and they agree on how

    to put information into these um into to put information into these um into to
    put information into these um into

    this format and uh because it''s being this format and uh because it''s being
    this format and uh because it''s being

    it''s like the bits are not ones and it''s like the bits are not ones and it''s
    like the bits are not ones and

    zeros in like a you know in a register zeros in like a you know in a register
    zeros in like a you know in a register

    or in or in a RAM cell um the uh like or in or in a RAM cell um the uh like'
  concept_slugs: []
- idx: 5
  start_sec: 226.239
  end_sec: 266.39
  text: 'or in or in a RAM cell um the uh like

    the manner in which the information is the manner in which the information is
    the manner in which the information is

    encoded is a little bit more complicated encoded is a little bit more complicated
    encoded is a little bit more complicated

    and it it has a couple of pieces. one is and it it has a couple of pieces. one
    is and it it has a couple of pieces. one is

    like uh when you point at this you need like uh when you point at this you need
    like uh when you point at this you need

    to figure out where the bits start and to figure out where the bits start and
    to figure out where the bits start and

    end. So you have these big squares. Um end. So you have these big squares. Um
    end. So you have these big squares. Um

    and then second is that there''s very and then second is that there''s very and
    then second is that there''s very

    heavy error correction on this. So heavy error correction on this. So heavy error
    correction on this. So

    instead of just putting you know black instead of just putting you know black
    instead of just putting you know black

    and white as ones and zeros, the sort of and white as ones and zeros, the sort
    of and white as ones and zeros, the sort of

    like naive way you might do it um you like naive way you might do it um you like
    naive way you might do it um you

    there''s there''s error correction just as there''s there''s error correction
    just as there''s there''s error correction just as

    you have error correcting codes for you have error correcting codes for you have
    error correcting codes for

    transmission on networks or when you transmission on networks or when you transmission
    on networks or when you

    have very unreliable uh RAM inside of a have very unreliable uh RAM inside of
    a have very unreliable uh RAM inside of a

    system. Uh, and so it''s designed for system. Uh, and so it''s designed for system.
    Uh, and so it''s designed for

    this really high robustness because you this really high robustness because you
    this really high robustness because you

    you put these things out in the physical'
  concept_slugs: []
- idx: 6
  start_sec: 266.39
  end_sec: 306.8
  text: 'you put these things out in the physical you put these things out in the
    physical

    world and lighting conditions change or world and lighting conditions change or
    world and lighting conditions change or

    somebody like tears the piece of paper somebody like tears the piece of paper
    somebody like tears the piece of paper

    you printed the QR code on or whatever. you printed the QR code on or whatever.
    you printed the QR code on or whatever.

    Um, and you want to like be able to Um, and you want to like be able to Um, and
    you want to like be able to

    recover from this as gracefully as recover from this as gracefully as recover
    from this as gracefully as

    possible, right? I think that QR code possible, right? I think that QR code possible,
    right? I think that QR code

    still scans and goes to the Wikipedia still scans and goes to the Wikipedia still
    scans and goes to the Wikipedia

    page for QR codes. Um so what people you page for QR codes. Um so what people
    you page for QR codes. Um so what people you

    know the so that''s there''s like one view know the so that''s there''s like one
    view know the so that''s there''s like one view

    of like this robustness is for being of like this robustness is for being of like
    this robustness is for being

    able to communicate in uh sort of like able to communicate in uh sort of like
    able to communicate in uh sort of like

    high noise situations. Um but you know high noise situations. Um but you know
    high noise situations. Um but you know

    one one one man''s noise is another man''s one one one man''s noise is another
    man''s one one one man''s noise is another man''s

    signal right the key thing here is that signal right the key thing here is that
    signal right the key thing here is that

    you can also kind of like corrupt the you can also kind of like corrupt the you
    can also kind of like corrupt the

    information in a QR code. can put other information in a QR code. can put other
    information in a QR code. can put other

    uh images or other information into a QR uh images or other information into a
    QR'
  concept_slugs: []
- idx: 7
  start_sec: 306.8
  end_sec: 351.919
  text: 'uh images or other information into a QR

    code and so long as you you know leave code and so long as you you know leave
    code and so long as you you know leave

    the error correcting bits in place or the error correcting bits in place or the
    error correcting bits in place or

    make your edits very carefully uh then make your edits very carefully uh then
    make your edits very carefully uh then

    it''s still a scannable QR code. You can it''s still a scannable QR code. You
    can it''s still a scannable QR code. You can

    still take a QR code reader and retrieve still take a QR code reader and retrieve
    still take a QR code reader and retrieve

    the information from the QR code. Um so the information from the QR code. Um so
    the information from the QR code. Um so

    people used to do this sort of by hand people used to do this sort of by hand
    people used to do this sort of by hand

    and this is like a handmade corrupted QR and this is like a handmade corrupted
    QR and this is like a handmade corrupted QR

    code uh from the Wikipedia page. um uh code uh from the Wikipedia page. um uh
    code uh from the Wikipedia page. um uh

    but like with the rise of generative but like with the rise of generative but
    like with the rise of generative

    models of images, you can now do this models of images, you can now do this models
    of images, you can now do this

    automatically. So this image here is automatically. So this image here is automatically.
    So this image here is

    also a QR code. It''s no longer just also a QR code. It''s no longer just also
    a QR code. It''s no longer just

    black and white and it''s not black and black and white and it''s not black and
    black and white and it''s not black and

    white with some like handmade human white with some like handmade human white
    with some like handmade human

    edits. It''s a careful sort of like edits. It''s a careful sort of like edits.
    It''s a careful sort of like

    mixing of black, mostly black and mostly mixing of black, mostly black and mostly'
  concept_slugs: []
- idx: 8
  start_sec: 351.919
  end_sec: 392.96
  text: 'mixing of black, mostly black and mostly

    white blocks of pixels into a pattern white blocks of pixels into a pattern white
    blocks of pixels into a pattern

    for um uh that is also a uh it''s a QR for um uh that is also a uh it''s a QR
    for um uh that is also a uh it''s a QR

    code, but it''s also an image that if you code, but it''s also an image that if
    you code, but it''s also an image that if you

    look at it looks like a you know like a look at it looks like a you know like
    a look at it looks like a you know like a

    snowy Japanese village or something. Um snowy Japanese village or something. Um
    snowy Japanese village or something. Um

    and so this image was posted on Reddit and so this image was posted on Reddit
    and so this image was posted on Reddit

    like three years ago now I would say. like three years ago now I would say. like
    three years ago now I would say.

    Um, and uh, people got, you know, really Um, and uh, people got, you know, really
    Um, and uh, people got, you know, really

    excited, ran and like made a bunch of excited, ran and like made a bunch of excited,
    ran and like made a bunch of

    these kinds of images. Um, and the these kinds of images. Um, and the these kinds
    of images. Um, and the

    person who made it also made a website person who made it also made a website
    person who made it also made a website

    where you could generate QR codes. So I where you could generate QR codes. So
    I where you could generate QR codes. So I

    went on and tried to generate a QR code went on and tried to generate a QR code
    went on and tried to generate a QR code

    and this is like I wanted an image of and this is like I wanted an image of and
    this is like I wanted an image of

    fireworks and I wanted to make a fireworks and I wanted to make a fireworks and
    I wanted to make a

    scannable QR code with it. Um, and it scannable QR code with it. Um, and it'
  concept_slugs: []
- idx: 9
  start_sec: 392.96
  end_sec: 433.28
  text: 'scannable QR code with it. Um, and it

    failed. Like this image, there''s not failed. Like this image, there''s not failed.
    Like this image, there''s not

    enough, you know, the dark and light enough, you know, the dark and light enough,
    you know, the dark and light

    patterns in this image don''t actually patterns in this image don''t actually
    patterns in this image don''t actually

    line up with the QR code. So they it''s line up with the QR code. So they it''s
    line up with the QR code. So they it''s

    not a it''s like an attempt at making a not a it''s like an attempt at making
    a not a it''s like an attempt at making a

    QR code but it''s failed right and if QR code but it''s failed right and if QR
    code but it''s failed right and if

    you''ve tried to build any ML you''ve tried to build any ML you''ve tried to build
    any ML

    applications whether it''s like you''re applications whether it''s like you''re
    applications whether it''s like you''re

    using a coding agent or you''re asking a using a coding agent or you''re asking
    a using a coding agent or you''re asking a

    chatbot to do like you know support or chatbot to do like you know support or
    chatbot to do like you know support or

    answer questions help you with your answer questions help you with your answer
    questions help you with your

    homework or you''re building like you homework or you''re building like you homework
    or you''re building like you

    know art generation with diffusion know art generation with diffusion know art
    generation with diffusion

    models you know that like these things models you know that like these things
    models you know that like these things

    mess up they don''t do the thing that you mess up they don''t do the thing that
    you mess up they don''t do the thing that you

    anticipated anticipated anticipated

    um and then you have a problem of like um and then you have a problem of like
    um and then you have a problem of like

    yeah how do I fix this [clears throat] yeah how do I fix this [clears throat]
    yeah how do I fix this [clears throat]

    Um so the like core question that Um so the like core question that'
  concept_slugs: []
- idx: 10
  start_sec: 433.28
  end_sec: 478.71
  text: 'Um so the like core question that

    motivated this project was like can we motivated this project was like can we
    motivated this project was like can we

    make QR codes that look good and make QR codes that look good and make QR codes
    that look good and

    actually scan? Um and the answer is yes. actually scan? Um and the answer is yes.
    actually scan? Um and the answer is yes.

    We were able to like massively improve We were able to like massively improve
    We were able to like massively improve

    both the like rated aesthetic quality both the like rated aesthetic quality both
    the like rated aesthetic quality

    and the predicted aesthetic quality um and the predicted aesthetic quality um
    and the predicted aesthetic quality um

    according to an automated system and the according to an automated system and
    the according to an automated system and the

    uh scan rate uh of QR codes. So I''m uh scan rate uh of QR codes. So I''m uh scan
    rate uh of QR codes. So I''m

    going to walk you through the like basic going to walk you through the like basic
    going to walk you through the like basic

    approach. Um yeah, so we started off approach. Um yeah, so we started off approach.
    Um yeah, so we started off

    like the early version of this um like the early version of this um like the early
    version of this um

    generated these things that were like generated these things that were like generated
    these things that were like

    kind of okay at scanning but like pretty kind of okay at scanning but like pretty
    kind of okay at scanning but like pretty

    ugly. So this is like fireworks over a ugly. So this is like fireworks over a
    ugly. So this is like fireworks over a

    cityscape. And if you like really squint cityscape. And if you like really squint
    cityscape. And if you like really squint

    and look at it from far away, I guess it and look at it from far away, I guess
    it and look at it from far away, I guess it

    kind of looks like a city. Um and kind of looks like a city. Um and kind of looks
    like a city. Um and

    improving like more models came out a'
  concept_slugs: []
- idx: 11
  start_sec: 478.71
  end_sec: 520.959
  text: 'improving like more models came out a improving like more models came out
    a

    couple months later. Some people did couple months later. Some people did couple
    months later. Some people did

    some uh additional control net tuning some uh additional control net tuning some
    uh additional control net tuning

    and things got like a little bit better. and things got like a little bit better.
    and things got like a little bit better.

    Um but then we sat down and did some uh Um but then we sat down and did some uh
    Um but then we sat down and did some uh

    applied some extra tuning uh based off applied some extra tuning uh based off
    applied some extra tuning uh based off

    of some like carefully curated evals and of some like carefully curated evals
    and of some like carefully curated evals and

    applied uh some inference time comput applied uh some inference time comput applied
    uh some inference time comput

    scaling and we''re able to get results scaling and we''re able to get results
    scaling and we''re able to get results

    like the one all the way on the right uh like the one all the way on the right
    uh like the one all the way on the right uh

    where there''s clearly a city with where there''s clearly a city with where there''s
    clearly a city with

    fireworks above it and and is also like fireworks above it and and is also like
    fireworks above it and and is also like

    really um high uh the out this one scans really um high uh the out this one scans
    really um high uh the out this one scans

    very nicely and and the outputs have a very nicely and and the outputs have a
    very nicely and and the outputs have a

    high probability of scanning. Um so to high probability of scanning. Um so to
    high probability of scanning. Um so to

    walk through the like key secret sauce walk through the like key secret sauce
    walk through the like key secret sauce

    to that makes this work. Um like when to that makes this work. Um like when to
    that makes this work. Um like when

    you do when we do inference in the third you do when we do inference in the third'
  concept_slugs: []
- idx: 12
  start_sec: 520.959
  end_sec: 563.519
  text: 'you do when we do inference in the third

    system, [clears throat] we generate system, [clears throat] we generate system,
    [clears throat] we generate

    multiple outputs, multiple QR codes for multiple outputs, multiple QR codes for
    multiple outputs, multiple QR codes for

    for the same uh like text we want to put for the same uh like text we want to
    put for the same uh like text we want to put

    in the code and the same prompt. So we in the code and the same prompt. So we
    in the code and the same prompt. So we

    generate a bunch of them and then we generate a bunch of them and then we generate
    a bunch of them and then we

    like simulate we run a QR code scanner like simulate we run a QR code scanner
    like simulate we run a QR code scanner

    on a computer. Now again like a QR code on a computer. Now again like a QR code
    on a computer. Now again like a QR code

    is meant to be scanned in the physical is meant to be scanned in the physical
    is meant to be scanned in the physical

    world by like a phone or something like world by like a phone or something like
    world by like a phone or something like

    that, a camera in the physical world. So that, a camera in the physical world.
    So that, a camera in the physical world. So

    this is this is a simulation of that. Um this is this is a simulation of that.
    Um this is this is a simulation of that. Um

    and so you have to make sure your and so you have to make sure your and so you
    have to make sure your

    simulation is good. Um but we we run a simulation is good. Um but we we run a
    simulation is good. Um but we we run a

    simulation of scanning the QR code. Um, simulation of scanning the QR code. Um,
    simulation of scanning the QR code. Um,

    and then that gives us some fraction and then that gives us some fraction and
    then that gives us some fraction

    that we think we''ll scan. And then we that we think we''ll scan. And then we'
  concept_slugs: []
- idx: 13
  start_sec: 563.519
  end_sec: 602.56
  text: 'that we think we''ll scan. And then we

    take a look at those and we rank them by take a look at those and we rank them
    by take a look at those and we rank them by

    our uh by like an aesthetic score our uh by like an aesthetic score our uh by
    like an aesthetic score

    predictor. Um, a simple linear model on predictor. Um, a simple linear model on
    predictor. Um, a simple linear model on

    top of embeddings is good enough. Um, top of embeddings is good enough. Um, top
    of embeddings is good enough. Um,

    and here like thinking from like a user and here like thinking from like a user
    and here like thinking from like a user

    interaction perspective, you we''re the interaction perspective, you we''re the
    interaction perspective, you we''re the

    key thing users care about is they want key thing users care about is they want
    key thing users care about is they want

    to make sure that if they''re generating to make sure that if they''re generating
    to make sure that if they''re generating

    a QR code, it''s going to scan. That''s a QR code, it''s going to scan. That''s
    a QR code, it''s going to scan. That''s

    like, you know, the the cynic oneonone. like, you know, the the cynic oneonone.
    like, you know, the the cynic oneonone.

    That''s the that''s the if it''s um you That''s the that''s the if it''s um you
    That''s the that''s the if it''s um you

    know if it doesn''t scan then it''s not a know if it doesn''t scan then it''s
    not a know if it doesn''t scan then it''s not a

    QR code it''s just like a kind of ugly QR code it''s just like a kind of ugly
    QR code it''s just like a kind of ugly

    picture right um so that''s the key step picture right um so that''s the key step
    picture right um so that''s the key step

    for like sort of filtering and then the for like sort of filtering and then the
    for like sort of filtering and then the

    aesthetic ranking is a little bit less aesthetic ranking is a little bit less
    aesthetic ranking is a little bit less

    important it''s just sort of like we want important it''s just sort of like we
    want'
  concept_slugs: []
- idx: 14
  start_sec: 602.56
  end_sec: 639.279
  text: 'important it''s just sort of like we want

    to show we want to put our best foot to show we want to put our best foot to show
    we want to put our best foot

    forward make it faster for the user to forward make it faster for the user to
    forward make it faster for the user to

    find one that they like um so that''s find one that they like um so that''s find
    one that they like um so that''s

    like that''s a little bit uh less less like that''s a little bit uh less less
    like that''s a little bit uh less less

    key in the in the design of the system key in the in the design of the system
    key in the in the design of the system

    um but yeah so that''s the that''s like um but yeah so that''s the that''s like
    um but yeah so that''s the that''s like

    core idea core idea core idea

    uh the idea is not super hard. We''ll uh the idea is not super hard. We''ll uh
    the idea is not super hard. We''ll

    talk a little bit about what exactly it talk a little bit about what exactly it
    talk a little bit about what exactly it

    took to implement that and learn some took to implement that and learn some took
    to implement that and learn some

    like general lessons about ML along the like general lessons about ML along the
    like general lessons about ML along the

    way. Um so, oh yeah, and by the way, way. Um so, oh yeah, and by the way, way.
    Um so, oh yeah, and by the way,

    like this, uh this thing is actually like this, uh this thing is actually like
    this, uh this thing is actually

    deployed. Uh you know, we''re a cloud deployed. Uh you know, we''re a cloud deployed.
    Uh you know, we''re a cloud

    infrastructure platform, so when I make infrastructure platform, so when I make
    infrastructure platform, so when I make

    a fun little toy like this, like I can a fun little toy like this, like I can
    a fun little toy like this, like I can

    actually deploy it. Um so, if you can actually deploy it. Um so, if you can'
  concept_slugs: []
- idx: 15
  start_sec: 639.279
  end_sec: 674.16
  text: 'actually deploy it. Um so, if you can

    see on my camera, I''m actually leaning a see on my camera, I''m actually leaning
    a see on my camera, I''m actually leaning a

    little bit back to scan the QR code. Um, little bit back to scan the QR code.
    Um, little bit back to scan the QR code. Um,

    that''s actually something a fun thing that''s actually something a fun thing
    that''s actually something a fun thing

    that I''ve discovered with these. Um, that I''ve discovered with these. Um, that
    I''ve discovered with these. Um,

    like if you look at them, the closer you like if you look at them, the closer
    you like if you look at them, the closer you

    get to them, the less they look like a get to them, the less they look like a
    get to them, the less they look like a

    QR code and the more they look like kind QR code and the more they look like kind
    QR code and the more they look like kind

    of a funky image. Um, and like a similar of a funky image. Um, and like a similar
    of a funky image. Um, and like a similar

    sort of um, like optical illusion or sort of um, like optical illusion or sort
    of um, like optical illusion or

    blurring effect also works on QR code blurring effect also works on QR code blurring
    effect also works on QR code

    readers. Um, which is kind of funny. readers. Um, which is kind of funny. readers.
    Um, which is kind of funny.

    It''s the reverse of a normal QR code It''s the reverse of a normal QR code It''s
    the reverse of a normal QR code

    reader where you want to get closer in reader where you want to get closer in
    reader where you want to get closer in

    order to increase the scan rate. But order to increase the scan rate. But order
    to increase the scan rate. But

    anyway, so I just scanned it and if I anyway, so I just scanned it and if I anyway,
    so I just scanned it and if I

    leaned back a little bit, my it uh it leaned back a little bit, my it uh it'
  concept_slugs: []
- idx: 16
  start_sec: 674.16
  end_sec: 710.64
  text: 'leaned back a little bit, my it uh it

    worked nicely for me. Um, you know, if I worked nicely for me. Um, you know, if
    I worked nicely for me. Um, you know, if I

    were in person and could see everybody, were in person and could see everybody,
    were in person and could see everybody,

    I''d ask folks to raise their hands on I''d ask folks to raise their hands on
    I''d ask folks to raise their hands on

    how many uh how many people were able to how many uh how many people were able
    to how many uh how many people were able to

    successfully scan it? Uh, I guess Kelly, successfully scan it? Uh, I guess Kelly,
    successfully scan it? Uh, I guess Kelly,

    uh, are folks able to scan it in the in uh, are folks able to scan it in the in
    uh, are folks able to scan it in the in

    the lecture hall? the lecture hall? the lecture hall?

    >> Yeah. Yeah, I think I think I Yeah, I >> Yeah. Yeah, I think I think I Yeah,
    I >> Yeah. Yeah, I think I think I Yeah, I

    think everyone was able to scan it. think everyone was able to scan it. think
    everyone was able to scan it.

    Well, I was able to scan it. So, Well, I was able to scan it. So, Well, I was
    able to scan it. So,

    >> great. Um, yeah. So, it''s fun like um >> great. Um, yeah. So, it''s fun like
    um >> great. Um, yeah. So, it''s fun like um

    I''m kind of like jumping a little bit I''m kind of like jumping a little bit
    I''m kind of like jumping a little bit

    ahead here, but one of the fun things ahead here, but one of the fun things ahead
    here, but one of the fun things

    about this is like you know you change about this is like you know you change
    about this is like you know you change

    the light like you you do some like data the light like you you do some like data
    the light like you you do some like data

    set collection, you do some alignment uh set collection, you do some alignment
    uh'
  concept_slugs: []
- idx: 17
  start_sec: 710.64
  end_sec: 754.32
  text: 'set collection, you do some alignment uh

    of your simulated system and and the of your simulated system and and the of your
    simulated system and and the

    real world and then like that gives you real world and then like that gives you
    real world and then like that gives you

    some you know probability of scanning some you know probability of scanning some
    you know probability of scanning

    but it''s it''s like subject to lighting but it''s it''s like subject to lighting
    but it''s it''s like subject to lighting

    conditions anyway. So much the these conditions anyway. So much the these conditions
    anyway. So much the these

    like uh the like data collection problem like uh the like data collection problem
    like uh the like data collection problem

    actually ends up always as always being actually ends up always as always being
    actually ends up always as always being

    like more uh more complicated than it like more uh more complicated than it like
    more uh more complicated than it

    seems when you first set out. Um yeah, seems when you first set out. Um yeah,
    seems when you first set out. Um yeah,

    so good good that folks were able to so good good that folks were able to so good
    good that folks were able to

    scan it. Um, so yeah, sorry I I''m scan it. Um, so yeah, sorry I I''m scan it.
    Um, so yeah, sorry I I''m

    borrowing these slides from another from borrowing these slides from another from
    borrowing these slides from another from

    another slide deck um where like spend a another slide deck um where like spend
    a another slide deck um where like spend a

    little bit more time kind of talking little bit more time kind of talking little
    bit more time kind of talking

    about um how diffusion models work, but about um how diffusion models work, but
    about um how diffusion models work, but

    you''re in this class so you either you''re in this class so you either you''re
    in this class so you either

    already know or somebody else is going already know or somebody else is going
    already know or somebody else is going

    to do a way better job. So the key thing to do a way better job. So the key thing'
  concept_slugs: []
- idx: 18
  start_sec: 754.32
  end_sec: 795.11
  text: 'to do a way better job. So the key thing

    we''re using diffusion models text we''re using diffusion models text we''re using
    diffusion models text

    condition generative model of images. Um condition generative model of images.
    Um condition generative model of images. Um

    we add a control net. Uh this uh I think we add a control net. Uh this uh I think
    we add a control net. Uh this uh I think

    these are coming back in style a little these are coming back in style a little
    these are coming back in style a little

    bit. the models that came out in the bit. the models that came out in the bit.
    the models that came out in the

    last couple months like the recent Flux last couple months like the recent Flux
    last couple months like the recent Flux

    Klein model for instance um have like Klein model for instance um have like Klein
    model for instance um have like

    better support for these but yeah they better support for these but yeah they
    better support for these but yeah they

    allow it''s like a separate component allow it''s like a separate component allow
    it''s like a separate component

    that allows you to guide generation not that allows you to guide generation not
    that allows you to guide generation not

    based on input text but based on an based on input text but based on an based
    on input text but based on an

    input image and not just like edit this input image and not just like edit this
    input image and not just like edit this

    image but like oh this image has a image but like oh this image has a image but
    like oh this image has a

    certain luminance pattern this image has certain luminance pattern this image
    has certain luminance pattern this image has

    a certain like color palette or pose and a certain like color palette or pose
    and a certain like color palette or pose and

    I want you to preserve that um in the I want you to preserve that um in the I
    want you to preserve that um in the

    output uh so we use a specific control output uh so we use a specific control
    output uh so we use a specific control

    net that''s actually fine-tuned for QR'
  concept_slugs: []
- idx: 19
  start_sec: 795.11
  end_sec: 835.67
  text: 'net that''s actually fine-tuned for QR net that''s actually fine-tuned for
    QR

    code generation. So like in theory, you code generation. So like in theory, you
    code generation. So like in theory, you

    could just use like a luminance control could just use like a luminance control
    could just use like a luminance control

    net and that says, hey, if I tell you to net and that says, hey, if I tell you
    to net and that says, hey, if I tell you to

    generate an image of a turtle, I''m also generate an image of a turtle, I''m also
    generate an image of a turtle, I''m also

    going to pass in this this an image with going to pass in this this an image with
    going to pass in this this an image with

    this luminance pattern and I want the this luminance pattern and I want the this
    luminance pattern and I want the

    image to have as close to this luminance image to have as close to this luminance
    image to have as close to this luminance

    pattern as possible. And that allows you pattern as possible. And that allows
    you pattern as possible. And that allows you

    to like generate an image that is both a to like generate an image that is both
    a to like generate an image that is both a

    turtle and uh has the QR codes luminance turtle and uh has the QR codes luminance
    turtle and uh has the QR codes luminance

    pattern and so can be scanned by a QR pattern and so can be scanned by a QR pattern
    and so can be scanned by a QR

    code scanner. Um, so l just using a code scanner. Um, so l just using a code scanner.
    Um, so l just using a

    regular luminance um, control net regular luminance um, control net regular luminance
    um, control net

    actually works okay here. Um, but actually works okay here. Um, but actually works
    okay here. Um, but

    there''s some some fine-tuned there''s some some fine-tuned there''s some some
    fine-tuned

    specifically on QR code generation that specifically on QR code generation that
    specifically on QR code generation that

    do even better. Um, so you can find do even better. Um, so you can find do even
    better. Um, so you can find

    those. They''re like scattered around'
  concept_slugs: []
- idx: 20
  start_sec: 835.67
  end_sec: 876.79
  text: 'those. They''re like scattered around those. They''re like scattered around

    picking face um, if you look around for picking face um, if you look around for
    picking face um, if you look around for

    them. Uh, yeah. So the key step first u them. Uh, yeah. So the key step first
    u them. Uh, yeah. So the key step first u

    if you want to do take an ML project if you want to do take an ML project if you
    want to do take an ML project

    that''s like promising but not working that''s like promising but not working
    that''s like promising but not working

    perfectly and you and you want to like perfectly and you and you want to like
    perfectly and you and you want to like

    kick it up a notch is you need to kick it up a notch is you need to kick it up
    a notch is you need to

    operationalize operationalize operationalize

    the things that you care about. Like the things that you care about. Like the
    things that you care about. Like

    usually ML projects have these like very usually ML projects have these like very
    usually ML projects have these like very

    fluffy goals. Like if you''re if you''re fluffy goals. Like if you''re if you''re
    fluffy goals. Like if you''re if you''re

    like a hardcore engineer, you''re used to like a hardcore engineer, you''re used
    to like a hardcore engineer, you''re used to

    things like I want the system to respond things like I want the system to respond
    things like I want the system to respond

    in 100 milliseconds and I want it to in 100 milliseconds and I want it to in 100
    milliseconds and I want it to

    consume no more than 70% of CPU cycles consume no more than 70% of CPU cycles
    consume no more than 70% of CPU cycles

    and like it needs to like fit this API. and like it needs to like fit this API.
    and like it needs to like fit this API.

    And these are these like very concrete And these are these like very concrete
    And these are these like very concrete

    and specific goals. But NL systems have and specific goals. But NL systems have
    and specific goals. But NL systems have

    goals like these users should be happy'
  concept_slugs: []
- idx: 21
  start_sec: 876.79
  end_sec: 921.59
  text: 'goals like these users should be happy goals like these users should be happy

    or like this this image should look or like this this image should look or like
    this this image should look

    good. um and like this image should be good. um and like this image should be
    good. um and like this image should be

    scannable by a QR code scannable by a QR code scannable by a QR code

    uh like compliant scanner um like a uh like compliant scanner um like a uh like
    compliant scanner um like a

    camera physical camera out in the world camera physical camera out in the world
    camera physical camera out in the world

    and these things are much looser uh in and these things are much looser uh in
    and these things are much looser uh in

    ML than than what you see in typical ML than than what you see in typical ML than
    than what you see in typical

    software and that''s like you know that''s software and that''s like you know
    that''s software and that''s like you know that''s

    why we try to solve these problems with why we try to solve these problems with
    why we try to solve these problems with

    machine learning because we don''t know machine learning because we don''t know
    machine learning because we don''t know

    how to write a computer program that how to write a computer program that how
    to write a computer program that

    does them from scratch so we train one does them from scratch so we train one
    does them from scratch so we train one

    based on data right so we we tend to get based on data right so we we tend to
    get based on data right so we we tend to get

    sort of sucked into these kinds of sort of sucked into these kinds of sort of
    sucked into these kinds of

    swamps or quagmires a as ML engineers swamps or quagmires a as ML engineers swamps
    or quagmires a as ML engineers

    because of the the kinds of things that because of the the kinds of things that
    because of the the kinds of things that

    we use machine learning on. we use machine learning on. we use machine learning
    on.

    Um so yeah so we need to operationalize'
  concept_slugs: []
- idx: 22
  start_sec: 921.59
  end_sec: 962.56
  text: 'Um so yeah so we need to operationalize Um so yeah so we need to operationalize

    these two goals. We also need to these two goals. We also need to these two goals.
    We also need to

    prioritize them as I alluded to earlier. prioritize them as I alluded to earlier.
    prioritize them as I alluded to earlier.

    The real thing that matters is we want The real thing that matters is we want
    The real thing that matters is we want

    to make sure that these QR codes scan to make sure that these QR codes scan to
    make sure that these QR codes scan

    because otherwise, you know, like people because otherwise, you know, like people
    because otherwise, you know, like people

    aren''t able to load the URL, people aren''t able to load the URL, people aren''t
    able to load the URL, people

    aren''t able to get on the Wi-Fi, people aren''t able to get on the Wi-Fi, people
    aren''t able to get on the Wi-Fi, people

    are mad. Uh, and the aesthetics are just are mad. Uh, and the aesthetics are just
    are mad. Uh, and the aesthetics are just

    like a bonus, right? Um, so that''s the like a bonus, right? Um, so that''s the
    like a bonus, right? Um, so that''s the

    sort of like order of our goals. sort of like order of our goals. sort of like
    order of our goals.

    Um, so the usual way things work in ML Um, so the usual way things work in ML
    Um, so the usual way things work in ML

    is you start out with an operational is you start out with an operational is you
    start out with an operational

    definition of your problem that''s very definition of your problem that''s very
    definition of your problem that''s very

    expensive and manual. Um so like in expensive and manual. Um so like in expensive
    and manual. Um so like in

    terms of looks good, we would maybe ask terms of looks good, we would maybe ask
    terms of looks good, we would maybe ask

    humans in uh some like setting to look humans in uh some like setting to look
    humans in uh some like setting to look

    at the images and assign a score to at the images and assign a score to'
  concept_slugs: []
- idx: 23
  start_sec: 962.56
  end_sec: 1005.269
  text: 'at the images and assign a score to

    them, right? And then that becomes our them, right? And then that becomes our
    them, right? And then that becomes our

    our operationalization of looks good. Um our operationalization of looks good.
    Um our operationalization of looks good. Um

    already like you''re thinking about like already like you''re thinking about like
    already like you''re thinking about like

    a number. It''s uh like you have to think a number. It''s uh like you have to
    think a number. It''s uh like you have to think

    about like numerical scales that''s like about like numerical scales that''s like
    about like numerical scales that''s like

    different than the like fluffier goal of different than the like fluffier goal
    of different than the like fluffier goal of

    of being aesthetically pleasing, but of being aesthetically pleasing, but of being
    aesthetically pleasing, but

    it''s it''s numerical and operational. Uh, it''s it''s numerical and operational.
    Uh, it''s it''s numerical and operational. Uh,

    and then scanning. We''re going to say and then scanning. We''re going to say
    and then scanning. We''re going to say

    that like a human moving an iPhone that like a human moving an iPhone that like
    a human moving an iPhone

    around in our office can scan the image. around in our office can scan the image.
    around in our office can scan the image.

    Um, so this is something, you know, this Um, so this is something, you know, this
    Um, so this is something, you know, this

    is expensive. Uh, but you can like at is expensive. Uh, but you can like at is
    expensive. Uh, but you can like at

    least uh you can at least run it. It''s a least uh you can at least run it. It''s
    a least uh you can at least run it. It''s a

    little bit more like a science little bit more like a science little bit more
    like a science

    experiment than it is um like something experiment than it is um like something
    experiment than it is um like something

    you could push to production, but at you could push to production, but at you
    could push to production, but at

    least it''s an operationalization. least it''s an operationalization. least it''s
    an operationalization.

    Uh and then the next step is you want to'
  concept_slugs: []
- idx: 24
  start_sec: 1005.269
  end_sec: 1050.95
  text: 'Uh and then the next step is you want to Uh and then the next step is you
    want to

    like automate these things you like automate these things you like automate these
    things you

    operationalized as much as possible. operationalized as much as possible. operationalized
    as much as possible.

    often by like using ML, right? Just as often by like using ML, right? Just as
    often by like using ML, right? Just as

    we when we make software, we write short we when we make software, we write short
    we when we make software, we write short

    snippets of software to test the snippets of software to test the snippets of
    software to test the

    software that we''re writing, we often software that we''re writing, we often
    software that we''re writing, we often

    use like smaller chunks of ML in order use like smaller chunks of ML in order
    use like smaller chunks of ML in order

    to improve the the core ML thing that to improve the the core ML thing that to
    improve the the core ML thing that

    we''re building, right? Like OpenAI''s we''re building, right? Like OpenAI''s
    we''re building, right? Like OpenAI''s

    flagship models are like GPD 5.2, flagship models are like GPD 5.2, flagship models
    are like GPD 5.2,

    but like it''s not like they just have but like it''s not like they just have
    but like it''s not like they just have

    one model. Like in the process of one model. Like in the process of one model.
    Like in the process of

    building that, they''ve got all kinds of building that, they''ve got all kinds
    of building that, they''ve got all kinds of

    things for synthetic data generation, things for synthetic data generation, things
    for synthetic data generation,

    for like Yeah. for reward modeling. All for like Yeah. for reward modeling. All
    for like Yeah. for reward modeling. All

    kinds of other ML models get included in kinds of other ML models get included
    in kinds of other ML models get included in

    there. Um, and so you you''ll probably there. Um, and so you you''ll probably
    there. Um, and so you you''ll probably

    end up doing the same things in your own end up doing the same things in your
    own end up doing the same things in your own

    ML projects. So we we want to have some'
  concept_slugs: []
- idx: 25
  start_sec: 1050.95
  end_sec: 1086.08
  text: 'ML projects. So we we want to have some ML projects. So we we want to have
    some

    sort of machine that will predict that sort of machine that will predict that
    sort of machine that will predict that

    humans assign high aesthetic scores or humans assign high aesthetic scores or
    humans assign high aesthetic scores or

    some machine that will predict that a some machine that will predict that a some
    machine that will predict that a

    human moving an iPhone around can scan human moving an iPhone around can scan
    human moving an iPhone around can scan

    it. So in both of these cases, we want it. So in both of these cases, we want
    it. So in both of these cases, we want

    to we''ll need to like sort of collect to we''ll need to like sort of collect
    to we''ll need to like sort of collect

    data on these things and then train a data on these things and then train a data
    on these things and then train a

    model. Um, so the good news on the first model. Um, so the good news on the first
    model. Um, so the good news on the first

    of our two goals, the one that''s less of our two goals, the one that''s less
    of our two goals, the one that''s less

    important is that there actually are important is that there actually are important
    is that there actually are

    reasonably good things out there from reasonably good things out there from reasonably
    good things out there from

    the like community of people who built the like community of people who built
    the like community of people who built

    diffusion models. We ran with this diffusion models. We ran with this diffusion
    models. We ran with this

    improved aesthetic predictor, which I improved aesthetic predictor, which I improved
    aesthetic predictor, which I

    think is from the Lyon people. Um, and think is from the Lyon people. Um, and
    think is from the Lyon people. Um, and

    that''s like that''s good enough. I mean, that''s like that''s good enough. I
    mean, that''s like that''s good enough. I mean,

    it''s not the most important thing in it''s not the most important thing in it''s
    not the most important thing in

    this project. So, we found something this project. So, we found something'
  concept_slugs: []
- idx: 26
  start_sec: 1086.08
  end_sec: 1135.51
  text: 'this project. So, we found something

    that worked well. Take a clip embedding that worked well. Take a clip embedding
    that worked well. Take a clip embedding

    small linear model on top of that. Um, small linear model on top of that. Um,
    small linear model on top of that. Um,

    for scanning, we looked around and we for scanning, we looked around and we for
    scanning, we looked around and we

    wanted to find a uh uh something that we wanted to find a uh uh something that
    we wanted to find a uh uh something that we

    could run um on uh you know run quickly could run um on uh you know run quickly
    could run um on uh you know run quickly

    and um would would uh like correlate and um would would uh like correlate and
    um would would uh like correlate

    pretty well with what people with the pretty well with what people with the pretty
    well with what people with the

    results you get from person with an results you get from person with an results
    you get from person with an

    iPhone in real life. We ended up running iPhone in real life. We ended up running
    iPhone in real life. We ended up running

    with this thing called Qreader which is with this thing called Qreader which is
    with this thing called Qreader which is

    has some YOLO computer vision models and has some YOLO computer vision models
    and has some YOLO computer vision models and

    combines those with a programmatic QR combines those with a programmatic QR combines
    those with a programmatic QR

    code reading library called Pisbar. code reading library called Pisbar. code reading
    library called Pisbar.

    Um so in order to make those choices uh Um so in order to make those choices uh
    Um so in order to make those choices uh

    we needed to sort of like collect some we needed to sort of like collect some
    we needed to sort of like collect some

    data to calibrate and to like like make data to calibrate and to like like make
    data to calibrate and to like like make

    sure that we believe that those two sure that we believe that those two sure that
    we believe that those two

    things were good. So I''d been running'
  concept_slugs: []
- idx: 27
  start_sec: 1135.51
  end_sec: 1172.08
  text: 'things were good. So I''d been running things were good. So I''d been running

    this thing in production and people had this thing in production and people had
    this thing in production and people had

    been using it for a while. Also, I was been using it for a while. Also, I was
    been using it for a while. Also, I was

    able to collect up a bunch of these um a able to collect up a bunch of these um
    a able to collect up a bunch of these um a

    bunch of these images and uh so I could bunch of these images and uh so I could
    bunch of these images and uh so I could

    run it on actually on QR codes generated run it on actually on QR codes generated
    run it on actually on QR codes generated

    by users. This was from the first by users. This was from the first by users.
    This was from the first

    version of the system that generated version of the system that generated version
    of the system that generated

    pretty ugly looking images but had like pretty ugly looking images but had like
    pretty ugly looking images but had like

    a reasonably high scan rate. Um so a reasonably high scan rate. Um so a reasonably
    high scan rate. Um so

    that''s why these images are so uh ugly. that''s why these images are so uh ugly.
    that''s why these images are so uh ugly.

    Um but yeah, so I was able to like I was Um but yeah, so I was able to like I
    was Um but yeah, so I was able to like I was

    able to measure our baseline, figure out able to measure our baseline, figure
    out able to measure our baseline, figure out

    where we we were at with these different where we we were at with these different
    where we we were at with these different

    tools. And so you know in the sort of tools. And so you know in the sort of tools.
    And so you know in the sort of

    you know highle version of this story you know highle version of this story you
    know highle version of this story

    people would say okay yeah you measure people would say okay yeah you measure'
  concept_slugs: []
- idx: 28
  start_sec: 1172.08
  end_sec: 1213.909
  text: 'people would say okay yeah you measure

    baseline with production data then you baseline with production data then you
    baseline with production data then you

    take your system parameters that you take your system parameters that you take
    your system parameters that you

    have and you just like sweep over them have and you just like sweep over them
    have and you just like sweep over them

    and you just hill climb on your eval and you just hill climb on your eval and
    you just hill climb on your eval

    metrics. Um but this is not the way metrics. Um but this is not the way metrics.
    Um but this is not the way

    things actually work in real life. like things actually work in real life. like
    things actually work in real life. like

    there''s a bunch of stuff that comes in there''s a bunch of stuff that comes in
    there''s a bunch of stuff that comes in

    between sort of like coming up with between sort of like coming up with between
    sort of like coming up with

    these um you know your evals or your these um you know your evals or your these
    um you know your evals or your

    your test suites um your your test suites um your your test suites um your

    operationalizations and actually like operationalizations and actually like operationalizations
    and actually like

    improving the system. So the first thing improving the system. So the first thing
    improving the system. So the first thing

    was to spend a bunch of time sitting was to spend a bunch of time sitting was
    to spend a bunch of time sitting

    there with these this system this model there with these this system this model
    there with these this system this model

    and just like digging around with all and just like digging around with all and
    just like digging around with all

    the parameters and like seeing what the parameters and like seeing what the parameters
    and like seeing what

    worked and what didn''t work. It was just worked and what didn''t work. It was
    just worked and what didn''t work. It was just

    like yeah and sort of like getting into like yeah and sort of like getting into
    like yeah and sort of like getting into

    the vibe of this system. A lot of ML'
  concept_slugs: []
- idx: 29
  start_sec: 1213.909
  end_sec: 1252.87
  text: 'the vibe of this system. A lot of ML the vibe of this system. A lot of ML

    systems are very they''re they''re like systems are very they''re they''re like
    systems are very they''re they''re like

    human approachable um and that gives you human approachable um and that gives
    you human approachable um and that gives you

    like and they''re very complex and so like and they''re very complex and so like
    and they''re very complex and so

    it''s a little bit more like you know it''s a little bit more like you know it''s
    a little bit more like you know

    music production where you kind of have music production where you kind of have
    music production where you kind of have

    to you have to hear the music um before to you have to hear the music um before
    to you have to hear the music um before

    you uh before you bring in the you uh before you bring in the you uh before you
    bring in the

    engineering. Um so that gave like a lot engineering. Um so that gave like a lot
    engineering. Um so that gave like a lot

    of like basically it helps you build of like basically it helps you build of like
    basically it helps you build

    intuition about the system that you''re intuition about the system that you''re
    intuition about the system that you''re

    working with and sort of identify which working with and sort of identify which
    working with and sort of identify which

    system parameters you even want to sweep system parameters you even want to sweep
    system parameters you even want to sweep

    over which matter and which don''t. Um, over which matter and which don''t. Um,
    over which matter and which don''t. Um,

    so the first was figuring out that this so the first was figuring out that this
    so the first was figuring out that this

    guidance scale parameter that I had kind guidance scale parameter that I had kind
    guidance scale parameter that I had kind

    of set based off of vibes and what of set based off of vibes and what of set based
    off of vibes and what

    people had put on the internet was like people had put on the internet was like
    people had put on the internet was like

    that was really important to get right.'
  concept_slugs: []
- idx: 30
  start_sec: 1252.87
  end_sec: 1294.24
  text: 'that was really important to get right. that was really important to get
    right.

    Um, kind of suspected it would be Um, kind of suspected it would be Um, kind of
    suspected it would be

    important to get right, but it was nice important to get right, but it was nice
    important to get right, but it was nice

    to get some confirmation from like like to get some confirmation from like like
    to get some confirmation from like like

    on anecdotally playing around with it. on anecdotally playing around with it.
    on anecdotally playing around with it.

    The second piece was a somewhat The second piece was a somewhat The second piece
    was a somewhat

    surprising parameter for for getting surprising parameter for for getting surprising
    parameter for for getting

    things that like felt good while we were things that like felt good while we were
    things that like felt good while we were

    generating codes was actually when does generating codes was actually when does
    generating codes was actually when does

    the control net get start getting the control net get start getting the control
    net get start getting

    applied during the like during the time applied during the like during the time
    applied during the like during the time

    steps of your diffusion. When do you steps of your diffusion. When do you steps
    of your diffusion. When do you

    start running the control net during start running the control net during start
    running the control net during

    that process? That''s actually super that process? That''s actually super that
    process? That''s actually super

    important for giving sort of this important for giving sort of this important
    for giving sort of this

    trade-off between letting the model be trade-off between letting the model be
    trade-off between letting the model be

    creative and making sure that it still creative and making sure that it still
    creative and making sure that it still

    hits this uh um you know scannability hits this uh um you know scannability hits
    this uh um you know scannability

    criterion. criterion. criterion.

    Um, so those turned out to be the like Um, so those turned out to be the like
    Um, so those turned out to be the like

    kind of key uh like key things to look kind of key uh like key things to look'
  concept_slugs: []
- idx: 31
  start_sec: 1294.24
  end_sec: 1332.07
  text: 'kind of key uh like key things to look

    at and that like this is super at and that like this is super at and that like
    this is super

    important. This step allows you to save important. This step allows you to save
    important. This step allows you to save

    a bunch of on compute later because a bunch of on compute later because a bunch
    of on compute later because

    instead of having 10 different instead of having 10 different instead of having
    10 different

    parameters they to sweep over a 100 parameters they to sweep over a 100 parameters
    they to sweep over a 100

    options for now maybe you you can like options for now maybe you you can like
    options for now maybe you you can like

    cut that down to just two. Um and and cut that down to just two. Um and and cut
    that down to just two. Um and and

    you know the search space that you have you know the search space that you have
    you know the search space that you have

    to go over grow grows uh you know to go over grow grows uh you know to go over
    grow grows uh you know

    exponentially uh multiplicatively you exponentially uh multiplicatively you exponentially
    uh multiplicatively you

    know as you add more parameters. And so know as you add more parameters. And so
    know as you add more parameters. And so

    you uh you definitely want to like keep you uh you definitely want to like keep
    you uh you definitely want to like keep

    that as small as possible. This by the that as small as possible. This by the
    that as small as possible. This by the

    way is also like generally good tip for way is also like generally good tip for
    way is also like generally good tip for

    your hyperparameter tuning. Um I''ve done your hyperparameter tuning. Um I''ve
    done your hyperparameter tuning. Um I''ve done

    a lot of model training in my time and a lot of model training in my time and
    a lot of model training in my time and

    if I have one piece of advice, it''s a if I have one piece of advice, it''s a
    if I have one piece of advice, it''s a

    it''s like apply this to your'
  concept_slugs: []
- idx: 32
  start_sec: 1332.07
  end_sec: 1369.28
  text: 'it''s like apply this to your it''s like apply this to your

    hyperparameter sweeps. Um sit down and hyperparameter sweeps. Um sit down and
    hyperparameter sweeps. Um sit down and

    figure out the reasonable range of figure out the reasonable range of figure out
    the reasonable range of

    parameters and the most and the like key parameters and the most and the like
    key parameters and the most and the like key

    parameters and and and focus on those. parameters and and and focus on those.
    parameters and and and focus on those.

    Um okay. So now, are we ready to sweep Um okay. So now, are we ready to sweep
    Um okay. So now, are we ready to sweep

    over system parameters? Like we picked over system parameters? Like we picked
    over system parameters? Like we picked

    these two that we think are important. these two that we think are important.
    these two that we think are important.

    Are we ready to just run a giant compute Are we ready to just run a giant compute
    Are we ready to just run a giant compute

    job and get our answer? Um, yeah. And to job and get our answer? Um, yeah. And
    to job and get our answer? Um, yeah. And to

    be clear, what does that compute job be clear, what does that compute job be clear,
    what does that compute job

    look like? We''ve got it. You know, we look like? We''ve got it. You know, we
    look like? We''ve got it. You know, we

    kind of want to run this like giant grid kind of want to run this like giant grid
    kind of want to run this like giant grid

    search uh on like, you know, if we were, search uh on like, you know, if we were,
    search uh on like, you know, if we were,

    this is like a famous picture of this is like a famous picture of this is like
    a famous picture of

    [clears throat] like figuring out the [clears throat] like figuring out the [clears
    throat] like figuring out the

    optimal like way to make toast um by optimal like way to make toast um by optimal
    like way to make toast um by

    like cook do you cook it for longer? Do like cook do you cook it for longer? Do'
  concept_slugs: []
- idx: 33
  start_sec: 1369.28
  end_sec: 1415.28
  text: 'like cook do you cook it for longer? Do

    you cook it at a higher temperature? Uh, you cook it at a higher temperature?
    Uh, you cook it at a higher temperature? Uh,

    right. So this is the way I''m going to right. So this is the way I''m going to
    right. So this is the way I''m going to

    display the data from our experiments as display the data from our experiments
    as display the data from our experiments as

    well. There''s going to be like our two well. There''s going to be like our two
    well. There''s going to be like our two

    axes of guidance scale and control axes of guidance scale and control axes of
    guidance scale and control

    guidance start time. Um and yeah, we''re guidance start time. Um and yeah, we''re
    guidance start time. Um and yeah, we''re

    going to have these big grids. Um so are going to have these big grids. Um so
    are going to have these big grids. Um so are

    we ready to to to run that big sweep? Um we ready to to to run that big sweep?
    Um we ready to to to run that big sweep? Um

    we are not. Uh first we like we want to we are not. Uh first we like we want to
    we are not. Uh first we like we want to

    go out and like label data so that we go out and like label data so that we go
    out and like label data so that we

    have uh like um uh so that we have a have uh like um uh so that we have a have
    uh like um uh so that we have a

    good baseline and this has to be done uh good baseline and this has to be done
    uh good baseline and this has to be done uh

    like by hand. Uh so like uh both like we like by hand. Uh so like uh both like
    we like by hand. Uh so like uh both like we

    want to run like to run this like huge want to run like to run this like huge
    want to run like to run this like huge

    sweep over a ton of options. We wanna we sweep over a ton of options. We wanna
    we'
  concept_slugs: []
- idx: 34
  start_sec: 1415.28
  end_sec: 1451.52
  text: 'sweep over a ton of options. We wanna we

    want to do that on like maybe tens of want to do that on like maybe tens of want
    to do that on like maybe tens of

    thousands hundreds of thousands of thousands hundreds of thousands of thousands
    hundreds of thousands of

    examples but like that would take like examples but like that would take like
    examples but like that would take like

    many many hours and it''s just like me many many hours and it''s just like me
    many many hours and it''s just like me

    like one or two engineers. We don''t have like one or two engineers. We don''t
    have like one or two engineers. We don''t have

    time for that. So we want to make sure time for that. So we want to make sure
    time for that. So we want to make sure

    that we''re like baseline calibrated with that we''re like baseline calibrated
    with that we''re like baseline calibrated with

    these uh with our with our QR code these uh with our with our QR code these uh
    with our with our QR code

    scanning uh metric and our uh like scanning uh metric and our uh like scanning
    uh metric and our uh like

    aesthetic predictor metric. So we do aesthetic predictor metric. So we do aesthetic
    predictor metric. So we do

    that on a small subset of the data. Um, that on a small subset of the data. Um,
    that on a small subset of the data. Um,

    and this part is also super important and this part is also super important and
    this part is also super important

    just like and and very manual just like just like and and very manual just like
    just like and and very manual just like

    sort of getting to know the system sort of getting to know the system sort of
    getting to know the system

    itself is is very important. Nobody itself is is very important. Nobody itself
    is is very important. Nobody

    really wants to sit down and look at the really wants to sit down and look at
    the really wants to sit down and look at the

    data, but you really got to do it. Um, data, but you really got to do it. Um,'
  concept_slugs: []
- idx: 35
  start_sec: 1451.52
  end_sec: 1488.48
  text: 'data, but you really got to do it. Um,

    so we sat down and sort of like uh you so we sat down and sort of like uh you
    so we sat down and sort of like uh you

    know vibe coded up a little setup where know vibe coded up a little setup where
    know vibe coded up a little setup where

    we could um indicate whether things we could um indicate whether things we could
    um indicate whether things

    whether images that were generated whether images that were generated whether
    images that were generated

    looked good and whether they scanned or looked good and whether they scanned or
    looked good and whether they scanned or

    not. Um, so yeah, let''s see. I''m not. Um, so yeah, let''s see. I''m not. Um,
    so yeah, let''s see. I''m

    actually going to jump forward a bit in actually going to jump forward a bit in
    actually going to jump forward a bit in

    these slides and say like what we found these slides and say like what we found
    these slides and say like what we found

    from like we you know we do this this from like we you know we do this this from
    like we you know we do this this

    round of like use like holding an iPhone round of like use like holding an iPhone
    round of like use like holding an iPhone

    up scanning things labeling them. First up scanning things labeling them. First
    up scanning things labeling them. First

    we found out that our implementation of we found out that our implementation of
    we found out that our implementation of

    our evals and and the library we were our evals and and the library we were our
    evals and and the library we were

    using had a had bugs in them and so we using had a had bugs in them and so we
    using had a had bugs in them and so we

    couldn''t run them on the on the large couldn''t run them on the on the large
    couldn''t run them on the on the large

    scale data and that was important. And scale data and that was important. And
    scale data and that was important. And

    it was like important to sit down and it was like important to sit down and'
  concept_slugs: []
- idx: 36
  start_sec: 1488.48
  end_sec: 1539.039
  text: 'it was like important to sit down and

    and look example by example and like and look example by example and like and
    look example by example and like

    detect that actually our evals had like detect that actually our evals had like
    detect that actually our evals had like

    regular old software engineering bugs in regular old software engineering bugs
    in regular old software engineering bugs in

    them. Uh basically it was like always them. Uh basically it was like always them.
    Uh basically it was like always

    showing up as like this thing the um uh showing up as like this thing the um uh
    showing up as like this thing the um uh

    the the the

    uh simulated scanner uh running on the uh simulated scanner uh running on the
    uh simulated scanner uh running on the

    machine was always scanning everything. machine was always scanning everything.
    machine was always scanning everything.

    Turned out we were handling null values Turned out we were handling null values
    Turned out we were handling null values

    incorrectly. And once we fixed that bug, incorrectly. And once we fixed that bug,
    incorrectly. And once we fixed that bug,

    we found that it was actually uh it was we found that it was actually uh it was
    we found that it was actually uh it was

    very well correlated with scanning. So very well correlated with scanning. So
    very well correlated with scanning. So

    this is a confusion matrix between the this is a confusion matrix between the
    this is a confusion matrix between the

    um our uh the simulated scanner and um our uh the simulated scanner and um our
    uh the simulated scanner and

    actual scans. And this is exactly the actual scans. And this is exactly the actual
    scans. And this is exactly the

    kind of confusion matrix you want to kind of confusion matrix you want to kind
    of confusion matrix you want to

    see. Very strong diagonal, very weak off see. Very strong diagonal, very weak
    off see. Very strong diagonal, very weak off

    diagonal. Um so that was like that step diagonal. Um so that was like that step
    diagonal. Um so that was like that step

    was important for building confidence in was important for building confidence
    in'
  concept_slugs: []
- idx: 37
  start_sec: 1539.039
  end_sec: 1582.159
  text: 'was important for building confidence in

    the actual like eval setup that we had. the actual like eval setup that we had.
    the actual like eval setup that we had.

    Um, and so then we could take a look at Um, and so then we could take a look at
    Um, and so then we could take a look at

    images like these, look at which ones images like these, look at which ones images
    like these, look at which ones

    were actually scanning under our uh with were actually scanning under our uh with
    were actually scanning under our uh with

    our new uh scanning system and which our new uh scanning system and which our
    new uh scanning system and which

    ones were not and look at the like ones were not and look at the like ones were
    not and look at the like

    aesthetic quality and try and pick the aesthetic quality and try and pick the
    aesthetic quality and try and pick the

    the like final parameters for guidance the like final parameters for guidance
    the like final parameters for guidance

    scale and control guidance start. Do I scale and control guidance start. Do I
    scale and control guidance start. Do I

    have more pictures of these? Oh yeah. Uh have more pictures of these? Oh yeah.
    Uh have more pictures of these? Oh yeah. Uh

    I do not. So the key insight was that if I do not. So the key insight was that
    if I do not. So the key insight was that if

    we picked there was like kind of a we picked there was like kind of a we picked
    there was like kind of a

    parameter setting which is I think parameter setting which is I think parameter
    setting which is I think

    corresponds to this block right here corresponds to this block right here corresponds
    to this block right here

    where we would pretty frequently see the where we would pretty frequently see
    the where we would pretty frequently see the

    things scanned we got like you know they things scanned we got like you know they
    things scanned we got like you know they

    we got like aesthetically pleasing we got like aesthetically pleasing we got like
    aesthetically pleasing

    results like it wasn''t as like as results like it wasn''t as like as'
  concept_slugs: []
- idx: 38
  start_sec: 1582.159
  end_sec: 1623.84
  text: 'results like it wasn''t as like as

    creative as some of the other settings creative as some of the other settings
    creative as some of the other settings

    that we saw but it was generating QR that we saw but it was generating QR that
    we saw but it was generating QR

    codes but it wasn''t as like overbaked as codes but it wasn''t as like overbaked
    as codes but it wasn''t as like overbaked as

    like maybe this setting in the top left like maybe this setting in the top left
    like maybe this setting in the top left

    where we like very frequently or this where we like very frequently or this where
    we like very frequently or this

    setting right here where like on all the setting right here where like on all
    the setting right here where like on all the

    examples that we tried we would get a QR examples that we tried we would get a
    QR examples that we tried we would get a QR

    code that''s scanned but like we didn''t code that''s scanned but like we didn''t
    code that''s scanned but like we didn''t

    the aesthetics were like a little bit the aesthetics were like a little bit the
    aesthetics were like a little bit

    too co QR cody and not uh QR cody and too co QR cody and not uh QR cody and too
    co QR cody and not uh QR cody and

    not arty enough. So this setting right not arty enough. So this setting right
    not arty enough. So this setting right

    here was where we landed. So we were here was where we landed. So we were here
    was where we landed. So we were

    able to improve the scan rate above the able to improve the scan rate above the
    able to improve the scan rate above the

    baseline settings while massively baseline settings while massively baseline settings
    while massively

    improving the like aesthetic quality. improving the like aesthetic quality. improving
    the like aesthetic quality.

    Um, so then, um, we wanted to come up Um, so then, um, we wanted to come up Um,
    so then, um, we wanted to come up

    with a way to like keep those settings with a way to like keep those settings'
  concept_slugs: []
- idx: 39
  start_sec: 1623.84
  end_sec: 1671.19
  text: 'with a way to like keep those settings

    but boost the overall scan rate for but boost the overall scan rate for but boost
    the overall scan rate for

    users. So the trick there was if we ran users. So the trick there was if we ran
    users. So the trick there was if we ran

    if you ran multiple times and take all if you ran multiple times and take all
    if you ran multiple times and take all

    of the results, the probability that of the results, the probability that of the
    results, the probability that

    none of the QR codes scan, that''s going none of the QR codes scan, that''s going
    none of the QR codes scan, that''s going

    to drop like multiplicatively that''s to drop like multiplicatively that''s to
    drop like multiplicatively that''s

    going to drop exponentially. So you so going to drop exponentially. So you so
    going to drop exponentially. So you so

    you start off with some settings where you start off with some settings where
    you start off with some settings where

    you have like say a one-/ird chance of you have like say a one-/ird chance of
    you have like say a one-/ird chance of

    failing and then you generate you know failing and then you generate you know
    failing and then you generate you know

    if you generate 32 of them you have like if you generate 32 of them you have like
    if you generate 32 of them you have like

    a one3 to the 30 to the 32 chance of of a one3 to the 30 to the 32 chance of of
    a one3 to the 30 to the 32 chance of of

    failing. Uh and so the key thing that failing. Uh and so the key thing that failing.
    Uh and so the key thing that

    makes that work for an actual deployed makes that work for an actual deployed
    makes that work for an actual deployed

    system is if you''ve taken this like system is if you''ve taken this like system
    is if you''ve taken this like

    evaluation system that you''ve built for evaluation system that you''ve built
    for evaluation system that you''ve built for

    tuning uh for like tuning your tuning uh for like tuning your tuning uh for like
    tuning your

    application, tuning your ML model, if'
  concept_slugs: []
- idx: 40
  start_sec: 1671.19
  end_sec: 1715.59
  text: 'application, tuning your ML model, if application, tuning your ML model,
    if

    you make that super super fast, you can you make that super super fast, you can
    you make that super super fast, you can

    just run it in production and then you just run it in production and then you
    just run it in production and then you

    can use it to evaluate the this like can use it to evaluate the this like can
    use it to evaluate the this like

    giant set of outputs that you''ve giant set of outputs that you''ve giant set
    of outputs that you''ve

    created. So in so then users don''t have created. So in so then users don''t have
    created. So in so then users don''t have

    to figure that out for themselves. to figure that out for themselves. to figure
    that out for themselves.

    Uh great. So with that in mind, we is Uh great. So with that in mind, we is Uh
    great. So with that in mind, we is

    how we ended up choosing these final how we ended up choosing these final how
    we ended up choosing these final

    system parameters which corresponds to system parameters which corresponds to
    system parameters which corresponds to

    this block right here. Um and we chose this block right here. Um and we chose
    this block right here. Um and we chose

    it specifically based off of like uh if it specifically based off of like uh if
    it specifically based off of like uh if

    we were to run I think eight eight we were to run I think eight eight we were
    to run I think eight eight

    generations, generations, generations,

    we could still hit our latency target. we could still hit our latency target.
    we could still hit our latency target.

    Running more generations in parallel Running more generations in parallel Running
    more generations in parallel

    tends to increase latency. So, we''d tends to increase latency. So, we''d tends
    to increase latency. So, we''d

    still hit our latency target, but we still hit our latency target, but we still
    hit our latency target, but we

    would also hit our uh an objective of of would also hit our uh an objective of
    of would also hit our uh an objective of of

    95% of the time on a set of test'
  concept_slugs: []
- idx: 41
  start_sec: 1715.59
  end_sec: 1762.559
  text: '95% of the time on a set of test 95% of the time on a set of test

    prompts, our uh the images, the QR prompts, our uh the images, the QR prompts,
    our uh the images, the QR

    codes, one of the QR codes would scan. codes, one of the QR codes would scan.
    codes, one of the QR codes would scan.

    Um, and so that''s shown in this chart Um, and so that''s shown in this chart
    Um, and so that''s shown in this chart

    here. So, we started off uh with like here. So, we started off uh with like here.
    So, we started off uh with like

    very ugly QR codes that had a reasonable very ugly QR codes that had a reasonable
    very ugly QR codes that had a reasonable

    chance of of scanning. Um, as models chance of of scanning. Um, as models chance
    of of scanning. Um, as models

    improved, aesthetics went up, but scan improved, aesthetics went up, but scan
    improved, aesthetics went up, but scan

    rate went down. And then adding this rate went down. And then adding this rate
    went down. And then adding this

    inference time compute scaling based off inference time compute scaling based
    off inference time compute scaling based off

    of with our eval selection allowed us to of with our eval selection allowed us
    to of with our eval selection allowed us to

    hit this like 95% scan rate. Um so and hit this like 95% scan rate. Um so and
    hit this like 95% scan rate. Um so and

    then all all throughout we were we''re then all all throughout we were we''re
    then all all throughout we were we''re

    able to do that without like able to do that without like able to do that without
    like

    compromising our aesthetic rating and compromising our aesthetic rating and compromising
    our aesthetic rating and

    like our our aesthetic rider kind of like our our aesthetic rider kind of like
    our our aesthetic rider kind of

    like saturates at around like six or like saturates at around like six or like
    saturates at around like six or

    seven. Um so there wasn''t a ton of seven. Um so there wasn''t a ton of seven.
    Um so there wasn''t a ton of

    headroom here. We probably could have headroom here. We probably could have'
  concept_slugs: []
- idx: 42
  start_sec: 1762.559
  end_sec: 1802.159
  text: 'headroom here. We probably could have

    done a better job if this were like an done a better job if this were like an
    done a better job if this were like an

    actual ML research project. we would actual ML research project. we would actual
    ML research project. we would

    have done a lot more work on the like have done a lot more work on the like have
    done a lot more work on the like

    aesthetic ranking here. So, this is this aesthetic ranking here. So, this is this
    aesthetic ranking here. So, this is this

    is more of the sort of like um like a is more of the sort of like um like a is
    more of the sort of like um like a

    vibe check or a backs stop to make sure vibe check or a backs stop to make sure
    vibe check or a backs stop to make sure

    things weren''t getting like terribly things weren''t getting like terribly things
    weren''t getting like terribly

    worse. worse. worse.

    Um so, yeah. So, um I''ll say I''ll I''ll Um so, yeah. So, um I''ll say I''ll
    I''ll Um so, yeah. So, um I''ll say I''ll I''ll

    come back to that. If you''re interested come back to that. If you''re interested
    come back to that. If you''re interested

    in this, if you want to hear like a in this, if you want to hear like a in this,
    if you want to hear like a

    little bit more uh detail and and see little bit more uh detail and and see little
    bit more uh detail and and see

    code uh and you can check out this blog code uh and you can check out this blog
    code uh and you can check out this blog

    post on [clears throat] our blog about post on [clears throat] our blog about
    post on [clears throat] our blog about

    this um that sort of yeah goes into more this um that sort of yeah goes into more
    this um that sort of yeah goes into more

    detail and links out to the code that we detail and links out to the code that
    we detail and links out to the code that we

    used for it. Um so that um yeah actually used for it. Um so that um yeah actually'
  concept_slugs: []
- idx: 43
  start_sec: 1802.159
  end_sec: 1862.71
  text: 'used for it. Um so that um yeah actually

    before I go any further any questions before I go any further any questions before
    I go any further any questions

    from folks in the audience about the um from folks in the audience about the um
    from folks in the audience about the um

    about what I just presented about the about what I just presented about the about
    what I just presented about the

    techniques that we used about this sort techniques that we used about this sort
    techniques that we used about this sort

    of like eval inference time scaling of like eval inference time scaling of like
    eval inference time scaling

    approach anything like that I guess I have a question. I guess I have a question.

    >> So you mentioned a lot about um you know >> So you mentioned a lot about um
    you know >> So you mentioned a lot about um you know

    just like hyperparameter tunings and just like hyperparameter tunings and just
    like hyperparameter tunings and

    like the most like I guess the very like the most like I guess the very like the
    most like I guess the very

    first bit that you mentioned was like first bit that you mentioned was like first
    bit that you mentioned was like

    vibe checking sort of right where you vibe checking sort of right where you vibe
    checking sort of right where you

    kind of just like look at images and see kind of just like look at images and
    see kind of just like look at images and see

    if there''s anything goes wrong. Um I if there''s anything goes wrong. Um I if
    there''s anything goes wrong. Um I

    guess I I mean like I also do that and guess I I mean like I also do that and
    guess I I mean like I also do that and

    think that''s like a very important skill think that''s like a very important
    skill think that''s like a very important skill

    for like image generation um like um for like image generation um like um for
    like image generation um like um

    research where you kind of just need to research where you kind of just need to
    research where you kind of just need to

    like be able to sniff if there''s'
  concept_slugs: []
- idx: 44
  start_sec: 1862.71
  end_sec: 1906.64
  text: 'like be able to sniff if there''s like be able to sniff if there''s

    anything goes wrong. Um so do you have anything goes wrong. Um so do you have
    anything goes wrong. Um so do you have

    any other like tips that like basically any other like tips that like basically
    any other like tips that like basically

    just like how do you usually manage um just like how do you usually manage um
    just like how do you usually manage um

    these kind of like vibe checking um these kind of like vibe checking um these
    kind of like vibe checking um

    experiments? experiments? experiments?

    >> Yeah. Yeah. There''s kind of like two >> Yeah. Yeah. There''s kind of like
    two >> Yeah. Yeah. There''s kind of like two

    pieces. One is like yeah, don''t let on pieces. One is like yeah, don''t let on
    pieces. One is like yeah, don''t let on

    the one hand like don''t let sort of like the one hand like don''t let sort of
    like the one hand like don''t let sort of like

    infrastructure get in your way and don''t infrastructure get in your way and don''t
    infrastructure get in your way and don''t

    let like perfectionism get in your way. let like perfectionism get in your way.
    let like perfectionism get in your way.

    You just want to like you want to make You just want to like you want to make
    You just want to like you want to make

    it as easy as possible for you to like it as easy as possible for you to like
    it as easy as possible for you to like

    look at outputs in a Jupyter notebook or look at outputs in a Jupyter notebook
    or look at outputs in a Jupyter notebook or

    an Excel spreadsheet or whatever. like an Excel spreadsheet or whatever. like
    an Excel spreadsheet or whatever. like

    you know uh and you might like if you''re you know uh and you might like if you''re
    you know uh and you might like if you''re

    you know especially if you''re still in you know especially if you''re still in
    you know especially if you''re still in

    school and taking like exciting classes school and taking like exciting classes
    school and taking like exciting classes

    about Bregman divergences or or whatever about Bregman divergences or or whatever'
  concept_slugs: []
- idx: 45
  start_sec: 1906.64
  end_sec: 1942.24
  text: 'about Bregman divergences or or whatever

    fancy math you might get excited about fancy math you might get excited about
    fancy math you might get excited about

    like oh how could I like come up with like oh how could I like come up with like
    oh how could I like come up with

    some like cool way to measure this thing some like cool way to measure this thing
    some like cool way to measure this thing

    and like you have to kind of turn that and like you have to kind of turn that
    and like you have to kind of turn that

    part of your brain off for a bit to like part of your brain off for a bit to like
    part of your brain off for a bit to like

    just you know just look at the look at just you know just look at the look at
    just you know just look at the look at

    the data just like yeah um be be a user the data just like yeah um be be a user
    the data just like yeah um be be a user

    or sort of like be a little bit more or sort of like be a little bit more or sort
    of like be a little bit more

    tightly intertwined with the system and tightly intertwined with the system and
    tightly intertwined with the system and

    and not let the sort of math get in your and not let the sort of math get in your
    and not let the sort of math get in your

    way. Uh then the other piece is yeah I way. Uh then the other piece is yeah I
    way. Uh then the other piece is yeah I

    used to work at weights and biases was used to work at weights and biases was
    used to work at weights and biases was

    there um pretty early on and like there there um pretty early on and like there
    there um pretty early on and like there

    the key thing that I really liked and the key thing that I really liked and the
    key thing that I really liked and

    that um I like pushed for in the way we that um I like pushed for in the way we'
  concept_slugs: []
- idx: 46
  start_sec: 1942.24
  end_sec: 1979.76
  text: 'that um I like pushed for in the way we

    designed the experiment management uh designed the experiment management uh designed
    the experiment management uh

    tooling that we built was you kind of tooling that we built was you kind of tooling
    that we built was you kind of

    just want to like dump as much just want to like dump as much just want to like
    dump as much

    information as possible into you know information as possible into you know information
    as possible into you know

    into some database some visualization into some database some visualization into
    some database some visualization

    system or into your Jupyter notebook or system or into your Jupyter notebook or
    system or into your Jupyter notebook or

    your Excel spreadsheet so that then like your Excel spreadsheet so that then like
    your Excel spreadsheet so that then like

    you can go back later and then recover you can go back later and then recover
    you can go back later and then recover

    and like find new patterns that you and like find new patterns that you and like
    find new patterns that you

    didn''t expect. So like rather than just didn''t expect. So like rather than just
    didn''t expect. So like rather than just

    like you know there''s this like like you know there''s this like like you know
    there''s this like

    temptation maybe to try and like cut temptation maybe to try and like cut temptation
    maybe to try and like cut

    down on what you log and like only log a down on what you log and like only log
    a down on what you log and like only log a

    small number of things as you''re going small number of things as you''re going
    small number of things as you''re going

    and and playing with your the system. Um and and playing with your the system.
    Um and and playing with your the system. Um

    but what you find out is that like but what you find out is that like but what
    you find out is that like

    months later you''re like oh wait there months later you''re like oh wait there
    months later you''re like oh wait there

    was a bug where like every time that was a bug where like every time that'
  concept_slugs: []
- idx: 47
  start_sec: 1979.76
  end_sec: 2017.919
  text: 'was a bug where like every time that

    this value was x like I I like this value was x like I I like this value was x
    like I I like

    mismanaged it. When did I introduce that mismanaged it. When did I introduce that
    mismanaged it. When did I introduce that

    bug? like and if you if the like higher bug? like and if you if the like higher
    bug? like and if you if the like higher

    cardality and the higher complexity of cardality and the higher complexity of
    cardality and the higher complexity of

    data that you log, the easier it is to data that you log, the easier it is to
    data that you log, the easier it is to

    like find out stuff post hawk. Um so I like find out stuff post hawk. Um so I
    like find out stuff post hawk. Um so I

    think of it as being sort of like I log think of it as being sort of like I log
    think of it as being sort of like I log

    I put up this like very initial thing I put up this like very initial thing I
    put up this like very initial thing

    that I can then like do projections of. that I can then like do projections of.
    that I can then like do projections of.

    If you like math, you know, it''s like a If you like math, you know, it''s like
    a If you like math, you know, it''s like a

    an initial algebra or an initial object an initial algebra or an initial object
    an initial algebra or an initial object

    that you do mapping out of. Um so that''s that you do mapping out of. Um so that''s
    that you do mapping out of. Um so that''s

    the way that I think also by the way the way that I think also by the way the
    way that I think also by the way

    about like logging for production about like logging for production about like
    logging for production

    systems. It''s like yeah log more than systems. It''s like yeah log more than
    systems. It''s like yeah log more than

    you think you''ll need and then be good you think you''ll need and then be good'
  concept_slugs: []
- idx: 48
  start_sec: 2017.919
  end_sec: 2066.869
  text: 'you think you''ll need and then be good

    at searching them. Um so like you know at searching them. Um so like you know
    at searching them. Um so like you know

    data dog and all these others uh sort of data dog and all these others uh sort
    of data dog and all these others uh sort of

    like encourage you to take that same like encourage you to take that same like
    encourage you to take that same

    approach to the sort of like management approach to the sort of like management
    approach to the sort of like management

    and and uptime and reliability and and and and uptime and reliability and and
    and and uptime and reliability and and

    improvement of of all kinds of software improvement of of all kinds of software
    improvement of of all kinds of software

    systems not just ML once. systems not just ML once. systems not just ML once.

    >> Cool. Amazing. >> Cool. Amazing. >> Cool. Amazing.

    >> Um cool. So uh I did this project >> Um cool. So uh I did this project >> Um
    cool. So uh I did this project

    actually before I joined modal. I was actually before I joined modal. I was actually
    before I joined modal. I was

    just I was uh looking around for just I was uh looking around for just I was uh
    looking around for

    infrastructure tools and and I wanted to infrastructure tools and and I wanted
    to infrastructure tools and and I wanted to

    build this QR code project and I and I build this QR code project and I and I
    build this QR code project and I and I

    landed on this particular infrastructure landed on this particular infrastructure
    landed on this particular infrastructure

    tool modal like yeah three years ago now tool modal like yeah three years ago
    now tool modal like yeah three years ago now

    I guess um and it was super helpful I guess um and it was super helpful I guess
    um and it was super helpful

    because I could do things like uh the because I could do things like uh the because
    I could do things like uh the

    inference time compute scaling piece inference time compute scaling piece inference
    time compute scaling piece

    it''s like I can just trade compute for'
  concept_slugs: []
- idx: 49
  start_sec: 2066.869
  end_sec: 2105.839
  text: 'it''s like I can just trade compute for it''s like I can just trade compute
    for

    quality so now I actually have this like quality so now I actually have this like
    quality so now I actually have this like

    I have an engineering control over I have an engineering control over I have an
    engineering control over

    quality and it''s like a cost quality quality and it''s like a cost quality quality
    and it''s like a cost quality

    tradeoff But at least I have like a knob tradeoff But at least I have like a knob
    tradeoff But at least I have like a knob

    I can turn. Um, and modal gave me like I can turn. Um, and modal gave me like
    I can turn. Um, and modal gave me like

    flexible infrastructure. I could use one flexible infrastructure. I could use
    one flexible infrastructure. I could use one

    GPU. I could use a B200 if I needed it. GPU. I could use a B200 if I needed it.
    GPU. I could use a B200 if I needed it.

    Or I could switch to just run on an A10. Or I could switch to just run on an A10.
    Or I could switch to just run on an A10.

    Um, and that allowed me to sort of also Um, and that allowed me to sort of also
    Um, and that allowed me to sort of also

    like trade off compute and uh quantity, like trade off compute and uh quantity,
    like trade off compute and uh quantity,

    the like quality of output, the cost, the like quality of output, the cost, the
    like quality of output, the cost,

    the whole thing. Um, also like this the whole thing. Um, also like this the whole
    thing. Um, also like this

    thing pretty quickly like we now have thing pretty quickly like we now have thing
    pretty quickly like we now have

    this like pis bar library that''s running this like pis bar library that''s running
    this like pis bar library that''s running

    YOLO models. There''s this aesthetic YOLO models. There''s this aesthetic YOLO
    models. There''s this aesthetic

    predictor. All these different things predictor. All these different things predictor.
    All these different things

    are there''s like multiple models that are there''s like multiple models that'
  concept_slugs: []
- idx: 50
  start_sec: 2105.839
  end_sec: 2141.76
  text: 'are there''s like multiple models that

    need to do the inference. The inference need to do the inference. The inference
    need to do the inference. The inference

    is also sort of yeah it''s deployed on a is also sort of yeah it''s deployed on
    a is also sort of yeah it''s deployed on a

    website. There''s some job management website. There''s some job management website.
    There''s some job management

    stuff. Um and I needed a compute stuff. Um and I needed a compute stuff. Um and
    I needed a compute

    platform that could do all of those platform that could do all of those platform
    that could do all of those

    pieces, not just like um you know not pieces, not just like um you know not pieces,
    not just like um you know not

    just an API that would give me you know just an API that would give me you know
    just an API that would give me you know

    stable diffusion outputs and let me stable diffusion outputs and let me stable
    diffusion outputs and let me

    upload my control net. I needed like upload my control net. I needed like upload
    my control net. I needed like

    full and total control. Um, and then full and total control. Um, and then full
    and total control. Um, and then

    when doing all the suites that we talked when doing all the suites that we talked
    when doing all the suites that we talked

    about, you know, we spent a lot of time, about, you know, we spent a lot of time,
    about, you know, we spent a lot of time,

    less time talking about the application less time talking about the application
    less time talking about the application

    and a lot of time talking about the and a lot of time talking about the and a
    lot of time talking about the

    evaluation and the hyperparameter evaluation and the hyperparameter evaluation
    and the hyperparameter

    tuning. Um, all that needed like very tuning. Um, all that needed like very tuning.
    Um, all that needed like very

    bursty compute. Like there was periods bursty compute. Like there was periods
    bursty compute. Like there was periods

    where all of a sudden if I had 100 GPUs, where all of a sudden if I had 100 GPUs,'
  concept_slugs: []
- idx: 51
  start_sec: 2141.76
  end_sec: 2179.119
  text: 'where all of a sudden if I had 100 GPUs,

    I could fill all 100 of those GPUs and I could fill all 100 of those GPUs and
    I could fill all 100 of those GPUs and

    then I would get an answer in 10 seconds then I would get an answer in 10 seconds
    then I would get an answer in 10 seconds

    or 30 seconds instead of like 30 minutes or 30 seconds instead of like 30 minutes
    or 30 seconds instead of like 30 minutes

    or uh, you know, or an hour if I were or uh, you know, or an hour if I were or
    uh, you know, or an hour if I were

    running it sequentially on a single GPU. running it sequentially on a single GPU.
    running it sequentially on a single GPU.

    But it''s not like I had a 100 GPUs worth But it''s not like I had a 100 GPUs
    worth But it''s not like I had a 100 GPUs worth

    of work all the time. Um, and so I of work all the time. Um, and so I of work
    all the time. Um, and so I

    needed to like scale up and down the needed to like scale up and down the needed
    to like scale up and down the

    amount of compute I was using uh like amount of compute I was using uh like amount
    of compute I was using uh like

    very quickly. Um, and so but like very quickly. Um, and so but like very quickly.
    Um, and so but like

    especially for those big sweeps where especially for those big sweeps where especially
    for those big sweeps where

    you know now I have like 10,000 images you know now I have like 10,000 images
    you know now I have like 10,000 images

    uh that I want to generate and I want to uh that I want to generate and I want
    to uh that I want to generate and I want to

    do that for like a 100 different do that for like a 100 different do that for
    like a 100 different

    settings of this parameter, 100 settings of this parameter, 100 settings of this
    parameter, 100

    different settings of this parameter different settings of this parameter'
  concept_slugs: []
- idx: 52
  start_sec: 2179.119
  end_sec: 2219.52
  text: 'different settings of this parameter

    like you can like that''s this sort of like you can like that''s this sort of
    like you can like that''s this sort of

    like embarrassingly parallel task. Um, like embarrassingly parallel task. Um,
    like embarrassingly parallel task. Um,

    so modal is the compute platform that I so modal is the compute platform that
    I so modal is the compute platform that I

    work on. Um, I like to think of it as AI work on. Um, I like to think of it as
    AI work on. Um, I like to think of it as AI

    infrastructure that doesn''t suck. Um, infrastructure that doesn''t suck. Um,
    infrastructure that doesn''t suck. Um,

    that is there to like actually help you that is there to like actually help you
    that is there to like actually help you

    solve the problems that you run into solve the problems that you run into solve
    the problems that you run into

    when you''re building um, you know, when you''re building um, you know, when you''re
    building um, you know,

    generative model applications, machine generative model applications, machine
    generative model applications, machine

    learning applications, and artificial learning applications, and artificial learning
    applications, and artificial

    intelligence. So, I''m actually going to intelligence. So, I''m actually going
    to intelligence. So, I''m actually going to

    start off. I''m just going to show like a start off. I''m just going to show like
    a start off. I''m just going to show like a

    quick code demo. Um, so I''m going to quick code demo. Um, so I''m going to quick
    code demo. Um, so I''m going to

    pull up my VS Code. Make that nice and pull up my VS Code. Make that nice and
    pull up my VS Code. Make that nice and

    big. Um, Kelly, do you think that that''s big. Um, Kelly, do you think that that''s
    big. Um, Kelly, do you think that that''s

    big enough or do you think it needs to big enough or do you think it needs to
    big enough or do you think it needs to

    be bigger for people to see it? be bigger for people to see it? be bigger for
    people to see it?

    >> Probably a little bit bigger, I think. >> Probably a little bit bigger, I think.'
  concept_slugs: []
- idx: 53
  start_sec: 2219.52
  end_sec: 2263.76
  text: '>> Probably a little bit bigger, I think.

    >> Oh, wow. Okay, we''re going full full >> Oh, wow. Okay, we''re going full full
    >> Oh, wow. Okay, we''re going full full

    zoom. zoom. zoom.

    >> Full um Yeah. Yes, that''s right. >> Full um Yeah. Yes, that''s right. >> Full
    um Yeah. Yes, that''s right.

    >> Okay. All right. Well, good thing that >> Okay. All right. Well, good thing
    that >> Okay. All right. Well, good thing that

    modal is only a few lines of code, or modal is only a few lines of code, or modal
    is only a few lines of code, or

    else it''d be hard to show it on this uh else it''d be hard to show it on this
    uh else it''d be hard to show it on this uh

    uh with this much zoom. Okay. So I''m uh with this much zoom. Okay. So I''m uh
    with this much zoom. Okay. So I''m

    just going to show you like what it just going to show you like what it just going
    to show you like what it

    looks like to use modal um to run stuff. looks like to use modal um to run stuff.
    looks like to use modal um to run stuff.

    Um so this is like a super simple Um so this is like a super simple Um so this
    is like a super simple

    example. So we help you run code on the example. So we help you run code on the
    example. So we help you run code on the

    cloud. You run code on the cloud by cloud. You run code on the cloud by cloud.
    You run code on the cloud by

    using our Python SDK to sort of like using our Python SDK to sort of like using
    our Python SDK to sort of like

    describe the like resources that you describe the like resources that you describe
    the like resources that you

    need in the cloud and um and how and need in the cloud and um and how and need
    in the cloud and um and how and

    like what code to run to use those like what code to run to use those like what
    code to run to use those

    resources to make your application. So resources to make your application. So'
  concept_slugs: []
- idx: 54
  start_sec: 2263.76
  end_sec: 2310.15
  text: 'resources to make your application. So

    you you could if you you start by you you you could if you you start by you you
    you could if you you start by you

    importing our Python SDK like creating importing our Python SDK like creating
    importing our Python SDK like creating

    an application and then often uh you an application and then often uh you an application
    and then often uh you

    know spending a couple hours wrangling know spending a couple hours wrangling
    know spending a couple hours wrangling

    with how to install you know with how to install you know with how to install
    you know

    transformers or diffusers or diffusers transformers or diffusers or diffusers
    transformers or diffusers or diffusers

    with a special patch to run flash with a special patch to run flash with a special
    patch to run flash

    tension 4 or whatever. Um so that''s this tension 4 or whatever. Um so that''s
    this tension 4 or whatever. Um so that''s this

    here. This is the compute environment here. This is the compute environment here.
    This is the compute environment

    that I want things to run in. that I want things to run in. that I want things
    to run in.

    Uh and then in order to make something Uh and then in order to make something
    Uh and then in order to make something

    that runs on modal, you basically take a that runs on modal, you basically take
    a that runs on modal, you basically take a

    Python function which looks something Python function which looks something Python
    function which looks something

    like this here. This is like a Python like this here. This is like a Python like
    this here. This is like a Python

    function that runs a language model. Um function that runs a language model. Um
    function that runs a language model. Um

    and then you add a decorator, a Python and then you add a decorator, a Python
    and then you add a decorator, a Python

    decorator like this one that says, hey, decorator like this one that says, hey,
    decorator like this one that says, hey,

    this is something that I want to run on this is something that I want to run on
    this is something that I want to run on

    the cloud. I want to run it on GPUs.'
  concept_slugs: []
- idx: 55
  start_sec: 2310.15
  end_sec: 2354.47
  text: 'the cloud. I want to run it on GPUs. the cloud. I want to run it on GPUs.

    That''s the particular type of GPU I want That''s the particular type of GPU I
    want That''s the particular type of GPU I want

    to use. And yeah, these are the like to use. And yeah, these are the like to use.
    And yeah, these are the like

    dependencies that I have. the the file dependencies that I have. the the file
    dependencies that I have. the the file

    system image or container image. Uh and system image or container image. Uh and
    system image or container image. Uh and

    then to just run like run a script, then to just run like run a script, then to
    just run like run a script,

    which is what you''ll probably do when which is what you''ll probably do when
    which is what you''ll probably do when

    you''re doing your like training runs or you''re doing your like training runs
    or you''re doing your like training runs or

    um uh like or if you''re like playing um uh like or if you''re like playing um
    uh like or if you''re like playing

    around with something, trying out around with something, trying out around with
    something, trying out

    different parameters by checking a different parameters by checking a different
    parameters by checking a

    model. Um then you hit this Python model. Um then you hit this Python model. Um
    then you hit this Python

    script with the modal run command. So script with the modal run command. So script
    with the modal run command. So

    using our command line interface and using our command line interface and using
    our command line interface and

    that will run this code on modal. So I''m that will run this code on modal. So
    I''m that will run this code on modal. So I''m

    going to scooch up a little bit here and going to scooch up a little bit here
    and going to scooch up a little bit here and

    show. So this is creating this remote show. So this is creating this remote show.
    So this is creating this remote

    function on modal getting a hold of a function on modal getting a hold of a function
    on modal getting a hold of a

    GPU. We''ve already done that. Um so like'
  concept_slugs: []
- idx: 56
  start_sec: 2354.47
  end_sec: 2399.829
  text: 'GPU. We''ve already done that. Um so like GPU. We''ve already done that.
    Um so like

    my code''s already running in the cloud. my code''s already running in the cloud.
    my code''s already running in the cloud.

    The container image was cached. Um so The container image was cached. Um so The
    container image was cached. Um so

    the container image is already ready and the container image is already ready
    and the container image is already ready and

    now hugging face transformers is loading now hugging face transformers is loading
    now hugging face transformers is loading

    up this 1.7 billion parameter language up this 1.7 billion parameter language
    up this 1.7 billion parameter language

    model and then passing uh a prompt in to model and then passing uh a prompt in
    to model and then passing uh a prompt in to

    do inference. Uh and so the prompt here do inference. Uh and so the prompt here
    do inference. Uh and so the prompt here

    is uh I actually just sent the code that is uh I actually just sent the code that
    is uh I actually just sent the code that

    we were just looking at to the model and we were just looking at to the model
    and we were just looking at to the model and

    asked it what does this code do and asked it what does this code do and asked
    it what does this code do and

    we''ve got our response. Okay. Yeah. Code we''ve got our response. Okay. Yeah.
    Code we''ve got our response. Okay. Yeah. Code

    defines a bodal function to run a defines a bodal function to run a defines a
    bodal function to run a

    chatbot that re that looks at the chatbot that re that looks at the chatbot that
    re that looks at the

    contents of the current um Python file. contents of the current um Python file.
    contents of the current um Python file.

    Um yeah function uses a G NH100 GPU and Um yeah function uses a G NH100 GPU and
    Um yeah function uses a G NH100 GPU and

    a DB and slim image. And we can take a a DB and slim image. And we can take a
    a DB and slim image. And we can take a

    look if we go to the modal um uh'
  concept_slugs: []
- idx: 57
  start_sec: 2399.829
  end_sec: 2438.96
  text: 'look if we go to the modal um uh look if we go to the modal um uh

    dashboard we can see there''s a bunch of dashboard we can see there''s a bunch
    of dashboard we can see there''s a bunch of

    like we have this nice like like we have this nice like like we have this nice
    like

    observability into what happened like observability into what happened like observability
    into what happened like

    the logs are all here. We have the logs are all here. We have the logs are all
    here. We have

    information about how long it took to information about how long it took to information
    about how long it took to

    get started. So it took us 3 seconds to get started. So it took us 3 seconds to
    get started. So it took us 3 seconds to

    go from running code at home to running go from running code at home to running
    go from running code at home to running

    code on modal and then it took 30 code on modal and then it took 30 code on modal
    and then it took 30

    seconds to run the actual inference. Um seconds to run the actual inference. Um
    seconds to run the actual inference. Um

    all kinds of neat metrics and things in all kinds of neat metrics and things in
    all kinds of neat metrics and things in

    here. We can see the GPU utilization. So here. We can see the GPU utilization.
    So here. We can see the GPU utilization. So

    if we zoom in here on the part when the if we zoom in here on the part when the
    if we zoom in here on the part when the

    prompt was running, we can see uh prompt was running, we can see uh prompt was
    running, we can see uh

    transformers is not a particularly super transformers is not a particularly super
    transformers is not a particularly super

    efficient at using the GPU. So even when efficient at using the GPU. So even when
    efficient at using the GPU. So even when

    it was running the prompt, we were only it was running the prompt, we were only
    it was running the prompt, we were only

    at 20% GPU utilization. That''s why at 20% GPU utilization. That''s why'
  concept_slugs: []
- idx: 58
  start_sec: 2438.96
  end_sec: 2479.28
  text: 'at 20% GPU utilization. That''s why

    people like to use things like VLM or people like to use things like VLM or people
    like to use things like VLM or

    SGLANG to run their language models. Uh SGLANG to run their language models. Uh
    SGLANG to run their language models. Uh

    I won''t go too deep into that since I won''t go too deep into that since I won''t
    go too deep into that since

    y''all are focused more on the diffusion y''all are focused more on the diffusion
    y''all are focused more on the diffusion

    models but um yeah anyway point is that models but um yeah anyway point is that
    models but um yeah anyway point is that

    you have all these metrics and things you have all these metrics and things you
    have all these metrics and things

    available. You can actually even go in available. You can actually even go in
    available. You can actually even go in

    here and find the code that that we just here and find the code that that we just
    here and find the code that that we just

    ran. So like all of that is available in ran. So like all of that is available
    in ran. So like all of that is available in

    the dashboard which is amazing. the code the dashboard which is amazing. the code
    the dashboard which is amazing. the code

    is being saved is especially super is being saved is especially super is being
    saved is especially super

    useful when you''re doing experimentation useful when you''re doing experimentation
    useful when you''re doing experimentation

    and like rapidly changing the code and and like rapidly changing the code and
    and like rapidly changing the code and

    you''re like wait which version of the you''re like wait which version of the
    you''re like wait which version of the

    code was I running when I got that code was I running when I got that code was
    I running when I got that

    result that you know has this result that you know has this result that you know
    has this

    interesting log. Um yeah so that''s the interesting log. Um yeah so that''s the
    interesting log. Um yeah so that''s the

    modal uh interface. Uh so then like modal uh interface. Uh so then like'
  concept_slugs: []
- idx: 59
  start_sec: 2479.28
  end_sec: 2518.48
  text: 'modal uh interface. Uh so then like

    that''s kind of cool but you know it''s that''s kind of cool but you know it''s
    that''s kind of cool but you know it''s

    not that hard to get a hold of a GPU as not that hard to get a hold of a GPU as
    not that hard to get a hold of a GPU as

    good as an H100. Um so you know what''s good as an H100. Um so you know what''s
    good as an H100. Um so you know what''s

    better than one H100? Like a 100 H100s. better than one H100? Like a 100 H100s.
    better than one H100? Like a 100 H100s.

    So this shows how to run that take that So this shows how to run that take that
    So this shows how to run that take that

    same prompt here, that same like uh that same prompt here, that same like uh that
    same prompt here, that same like uh that

    same uh chatbot same uh chatbot same uh chatbot

    uh uh application and run it like uh uh application and run it like uh uh application
    and run it like

    massively in parallel. So we just add a massively in parallel. So we just add
    a massively in parallel. So we just add a

    little bit of extra code down here. This little bit of extra code down here. This
    little bit of extra code down here. This

    runs on the local computer. So this is runs on the local computer. So this is
    runs on the local computer. So this is

    going to run on my laptop when I kick it going to run on my laptop when I kick
    it going to run on my laptop when I kick it

    off. And this is again sort of more the off. And this is again sort of more the
    off. And this is again sort of more the

    script style where we''ll hit this with script style where we''ll hit this with
    script style where we''ll hit this with

    modal run and it will look at like a modal run and it will look at like a modal
    run and it will look at like a

    hundred different Python files and send hundred different Python files and send'
  concept_slugs: []
- idx: 60
  start_sec: 2518.48
  end_sec: 2565.99
  text: 'hundred different Python files and send

    all hundred Python files to um to a all hundred Python files to um to a all hundred
    Python files to um to a

    chatbot and all we needed to do was take chatbot and all we needed to do was take
    chatbot and all we needed to do was take

    that modal function u and like map it that modal function u and like map it that
    modal function u and like map it

    over a Python iterator and it will run over a Python iterator and it will run
    over a Python iterator and it will run

    on all of them and we''ll like you''ll on all of them and we''ll like you''ll
    on all of them and we''ll like you''ll

    watch the the infrastructure just like watch the the infrastructure just like
    watch the the infrastructure just like

    auto magically scales up to match it. So auto magically scales up to match it.
    So auto magically scales up to match it. So

    let''s inference_map.py. let''s inference_map.py. let''s inference_map.py.

    So this is when you do your your So this is when you do your your So this is when
    you do your your

    hyperparameter sweep or when you want to hyperparameter sweep or when you want
    to hyperparameter sweep or when you want to

    run an eval on a bunch of data. All run an eval on a bunch of data. All run an
    eval on a bunch of data. All

    right. So we got we got 8 n 10 H100s right. So we got we got 8 n 10 H100s right.
    So we got we got 8 n 10 H100s

    have spun up. 12 13 14 15. So yeah. So have spun up. 12 13 14 15. So yeah. So
    have spun up. 12 13 14 15. So yeah. So

    these are now like I''m getting a hold of these are now like I''m getting a hold
    of these are now like I''m getting a hold of

    a bunch of GPUs running all of them in a bunch of GPUs running all of them in
    a bunch of GPUs running all of them in

    in parallel. Let me pull this up. Here''s in parallel. Let me pull this up. Here''s
    in parallel. Let me pull this up. Here''s

    the modal dashboard. We got 23 live'
  concept_slugs: []
- idx: 61
  start_sec: 2565.99
  end_sec: 2609.359
  text: 'the modal dashboard. We got 23 live the modal dashboard. We got 23 live

    containers. Let''s go and look at those. containers. Let''s go and look at those.
    containers. Let''s go and look at those.

    Oh yeah, look at all those. Look at all Oh yeah, look at all those. Look at all
    Oh yeah, look at all those. Look at all

    those GPUs. You love to see it. Um, and those GPUs. You love to see it. Um, and
    those GPUs. You love to see it. Um, and

    they are running all these inputs. And they are running all these inputs. And
    they are running all these inputs. And

    because these inputs are still running, because these inputs are still running,
    because these inputs are still running,

    modal is going to keep scaling up until modal is going to keep scaling up until
    modal is going to keep scaling up until

    we''re able to handle all the inputs that we''re able to handle all the inputs
    that we''re able to handle all the inputs that

    are coming in. Um, and we can see some are coming in. Um, and we can see some
    are coming in. Um, and we can see some

    of them, you''ll see little flashes of of them, you''ll see little flashes of
    of them, you''ll see little flashes of

    white text in here. That''s the response white text in here. That''s the response
    white text in here. That''s the response

    coming back from the model getting coming back from the model getting coming back
    from the model getting

    printed. Um, and so that same container printed. Um, and so that same container
    printed. Um, and so that same container

    will then get reused. So we''re topping will then get reused. So we''re topping
    will then get reused. So we''re topping

    out at about 50 or so uh H100s spun up. out at about 50 or so uh H100s spun up.
    out at about 50 or so uh H100s spun up.

    So each one handling probably like one So each one handling probably like one
    So each one handling probably like one

    maybe around two uh of these inputs. Um maybe around two uh of these inputs. Um
    maybe around two uh of these inputs. Um

    so yeah, so that''s um that''s sort of so yeah, so that''s um that''s sort of'
  concept_slugs: []
- idx: 62
  start_sec: 2609.359
  end_sec: 2653.68
  text: 'so yeah, so that''s um that''s sort of

    like fanning out and scaling out on like fanning out and scaling out on like fanning
    out and scaling out on

    modal um which you''ll probably run into modal um which you''ll probably run into
    modal um which you''ll probably run into

    if you want to do sort of like yeah if you want to do sort of like yeah if you
    want to do sort of like yeah

    training hyperparameter tuning um eval training hyperparameter tuning um eval
    training hyperparameter tuning um eval

    lots of those things sort of like lots of those things sort of like lots of those
    things sort of like

    running these big scripts. And the same running these big scripts. And the same
    running these big scripts. And the same

    basic infrastructure also helps you run basic infrastructure also helps you run
    basic infrastructure also helps you run

    an autoscaling application. So when like an autoscaling application. So when like
    an autoscaling application. So when like

    you know a b a bunch of users all show you know a b a bunch of users all show
    you know a b a bunch of users all show

    up to your website at the same time will up to your website at the same time will
    up to your website at the same time will

    also scale up more GPUs in a few seconds also scale up more GPUs in a few seconds
    also scale up more GPUs in a few seconds

    um to handle that like hug from Reddit um to handle that like hug from Reddit
    um to handle that like hug from Reddit

    or Twitter or uh whatever when you have or Twitter or uh whatever when you have
    or Twitter or uh whatever when you have

    a big uh scaling event. a big uh scaling event. a big uh scaling event.

    Um and yeah and all with just like a Um and yeah and all with just like a Um and
    yeah and all with just like a

    couple lines of Python which is pretty couple lines of Python which is pretty
    couple lines of Python which is pretty

    sick. Um and the same you know same sick. Um and the same you know same'
  concept_slugs: []
- idx: 63
  start_sec: 2653.68
  end_sec: 2705.359
  text: 'sick. Um and the same you know same

    basic uh tools that we use here you can basic uh tools that we use here you can
    basic uh tools that we use here you can

    use for your like for your you know use for your like for your you know use for
    your like for your you know

    messing around and and building out messing around and and building out messing
    around and and building out

    demos and PC''s and then also for demos and PC''s and then also for demos and
    PC''s and then also for

    deploying things to production at the deploying things to production at the deploying
    things to production at the

    scale of like scale of like scale of like

    exa like all kinds of different uh you exa like all kinds of different uh you
    exa like all kinds of different uh you

    know uh AI focused companies use modal know uh AI focused companies use modal
    know uh AI focused companies use modal

    for their production serving for their production serving for their production
    serving

    infrastructure. infrastructure. infrastructure.

    Um yeah actually so before I go any Um yeah actually so before I go any Um yeah
    actually so before I go any

    further in the talk uh any any questions further in the talk uh any any questions
    further in the talk uh any any questions

    or anything about like modal modal or anything about like modal modal or anything
    about like modal modal

    infrastructure and um the the problems infrastructure and um the the problems
    infrastructure and um the the problems

    it solves how to use it it solves how to use it it solves how to use it

    >> is there a way to run it in a Jupyter >> is there a way to run it in a Jupyter
    >> is there a way to run it in a Jupyter

    notebook type manner where it''s a very a notebook type manner where it''s a very
    a notebook type manner where it''s a very a

    lot more experimentative than me having lot more experimentative than me having
    lot more experimentative than me having

    to execute terminal commands having to to execute terminal commands having to
    to execute terminal commands having to

    send the code again run the code again send the code again run the code again'
  concept_slugs: []
- idx: 64
  start_sec: 2705.359
  end_sec: 2751.2
  text: 'send the code again run the code again

    >> right yeah that''s a Great question. So >> right yeah that''s a Great question.
    So >> right yeah that''s a Great question. So

    first uh so one is if you if you like first uh so one is if you if you like first
    uh so one is if you if you like

    terminals but you just want more terminals but you just want more terminals but
    you just want more

    interactive experience we can do modal interactive experience we can do modal
    interactive experience we can do modal

    shell into that same inferencemap.py shell into that same inferencemap.py shell
    into that same inferencemap.py

    and if I go into root here you''ll see and if I go into root here you''ll see
    and if I go into root here you''ll see

    inference map is in there and I should inference map is in there and I should
    inference map is in there and I should

    be able to just IPython. No we don''t be able to just IPython. No we don''t be
    able to just IPython. No we don''t

    have python. So let''s just like uh no have python. So let''s just like uh no
    have python. So let''s just like uh no

    pip install pip install Python, right? pip install pip install Python, right?
    pip install pip install Python, right?

    I''m doing this just to show you like you I''m doing this just to show you like
    you I''m doing this just to show you like you

    know a little bit of an interactive know a little bit of an interactive know a
    little bit of an interactive

    workflow here. Oh, I need this library. workflow here. Oh, I need this library.
    workflow here. Oh, I need this library.

    Let me just install it. This is like we Let me just install it. This is like we
    Let me just install it. This is like we

    spun up a new container. It''s a spun up a new container. It''s a spun up a new
    container. It''s a

    container with an H100 by the way. Um container with an H100 by the way. Um container
    with an H100 by the way. Um

    and we''re able to like, you know, and we''re able to like, you know,'
  concept_slugs: []
- idx: 65
  start_sec: 2751.2
  end_sec: 2800.88
  text: 'and we''re able to like, you know,

    around with it, change the change the around with it, change the change the around
    with it, change the change the

    settings, and it won''t mess our settings, and it won''t mess our settings, and
    it won''t mess our

    production infrastructure up, which is production infrastructure up, which is
    production infrastructure up, which is

    pretty sick. So I can do IP Python and pretty sick. So I can do IP Python and
    pretty sick. So I can do IP Python and

    then I should be able to import then I should be able to import then I should
    be able to import

    inference map. inference map. inference map.

    Oh yeah. So that that won''t quite work Oh yeah. So that that won''t quite work
    Oh yeah. So that that won''t quite work

    because I Yeah. Yeah. Okay. So that uh because I Yeah. Yeah. Okay. So that uh
    because I Yeah. Yeah. Okay. So that uh

    flew a little too close to the sun there flew a little too close to the sun there
    flew a little too close to the sun there

    trying a demo that I haven''t done trying a demo that I haven''t done trying a
    demo that I haven''t done

    before. But um so in many things you''d before. But um so in many things you''d
    before. But um so in many things you''d

    be able to import the code um like and be able to import the code um like and
    be able to import the code um like and

    um and run it and like play around with um and run it and like play around with
    um and run it and like play around with

    it from inside of a shell. Um then the it from inside of a shell. Um then the
    it from inside of a shell. Um then the

    other thing that we offer is modal other thing that we offer is modal other thing
    that we offer is modal

    notebooks. So modal.com notebooks. So modal.com notebooks. So modal.com

    notebooks. notebooks. notebooks.

    Um so these are so you can see here I Um so these are so you can see here I Um
    so these are so you can see here I

    was playing around with vl11 to try and was playing around with vl11 to try and'
  concept_slugs: []
- idx: 66
  start_sec: 2800.88
  end_sec: 2847.109
  text: 'was playing around with vl11 to try and

    maximize throughput. Um so uh and I was maximize throughput. Um so uh and I was
    maximize throughput. Um so uh and I was

    doing that on these uh these like doing that on these uh these like doing that
    on these uh these like

    filings that I got from an SEC filings that I got from an SEC filings that I got
    from an SEC

    uh uh endpoint the SEC Edgar feed and so uh uh endpoint the SEC Edgar feed and
    so uh uh endpoint the SEC Edgar feed and so

    there I like you know I needed to like there I like you know I needed to like
    there I like you know I needed to like

    inspect data it was very iterative so I inspect data it was very iterative so
    I inspect data it was very iterative so I

    ran it on these Jupyter notebooks. ran it on these Jupyter notebooks. ran it on
    these Jupyter notebooks.

    though for the data exploration stuff though for the data exploration stuff though
    for the data exploration stuff

    just a regular old Jupyter notebook CPU just a regular old Jupyter notebook CPU
    just a regular old Jupyter notebook CPU

    like you know nothing special no GPU or like you know nothing special no GPU or
    like you know nothing special no GPU or

    anything just a basic sort of collab anything just a basic sort of collab anything
    just a basic sort of collab

    style image um and then when I ran VLM I style image um and then when I ran VLM
    I style image um and then when I ran VLM I

    made sure to use the same like container made sure to use the same like container
    made sure to use the same like container

    image that I use in in production and to image that I use in in production and
    to image that I use in in production and to

    use in H100 and then played around with use in H100 and then played around with
    use in H100 and then played around with

    it again like it again like it again like

    um both playing around with the um both playing around with the um both playing
    around with the

    formatting of the data and then also'
  concept_slugs: []
- idx: 67
  start_sec: 2847.109
  end_sec: 2885.51
  text: 'formatting of the data and then also formatting of the data and then also

    playing around with all these like playing around with all these like playing
    around with all these like

    settings here that the OLM has to try settings here that the OLM has to try settings
    here that the OLM has to try

    and uh um get better performance and it and uh um get better performance and it
    and uh um get better performance and it

    was nice to have this sort of like was nice to have this sort of like was nice
    to have this sort of like

    iterative environment to do that in. Uh iterative environment to do that in. Uh
    iterative environment to do that in. Uh

    yeah, so great question. We have both of yeah, so great question. We have both
    of yeah, so great question. We have both of

    those. Check out notebooks are probably those. Check out notebooks are probably
    those. Check out notebooks are probably

    uh um the best option for doing training uh um the best option for doing training
    uh um the best option for doing training

    stuff with diffusion models uh because stuff with diffusion models uh because
    stuff with diffusion models uh because

    you''re going to want to take a look at you''re going to want to take a look at
    you''re going to want to take a look at

    the images. It''s a little hard to do the images. It''s a little hard to do the
    images. It''s a little hard to do

    that in a terminal, but not impossible that in a terminal, but not impossible
    that in a terminal, but not impossible

    if you''re, you know, a big terminal if you''re, you know, a big terminal if you''re,
    you know, a big terminal

    enjoyer. It can be done. I''ve done it a enjoyer. It can be done. I''ve done it
    a enjoyer. It can be done. I''ve done it a

    couple of times. It''s kind of fun. Um couple of times. It''s kind of fun. Um
    couple of times. It''s kind of fun. Um

    yeah. Any other questions? yeah. Any other questions? yeah. Any other questions?

    >> Uh I actually have a follow-up question. >> Uh I actually have a follow-up
    question. >> Uh I actually have a follow-up question.

    So say like because we''re already kind'
  concept_slugs: []
- idx: 68
  start_sec: 2885.51
  end_sec: 2935.28
  text: 'So say like because we''re already kind So say like because we''re already
    kind

    of like provided some like notebook of like provided some like notebook of like
    provided some like notebook

    skeleton for uh everyone. So is it skeleton for uh everyone. So is it skeleton
    for uh everyone. So is it

    possible for us to like just like upload possible for us to like just like upload
    possible for us to like just like upload

    like a normal Jupyter notebook and stuff like a normal Jupyter notebook and stuff
    like a normal Jupyter notebook and stuff

    and then just and then just and then just

    >> my god. >> my god. >> my god.

    >> Okay. >> Okay. >> Okay.

    >> Wow. I just want to say I never you know >> Wow. I just want to say I never
    you know >> Wow. I just want to say I never you know

    I''ve never met this woman before in my I''ve never met this woman before in my
    I''ve never met this woman before in my

    life. This is not a an audience plant. life. This is not a an audience plant.
    life. This is not a an audience plant.

    Um yeah if you there''s a Oops. There''s Um yeah if you there''s a Oops. There''s
    Um yeah if you there''s a Oops. There''s

    this import notebook button. If you this import notebook button. If you this import
    notebook button. If you

    enter, you can upload an IPython enter, you can upload an IPython enter, you can
    upload an IPython

    notebook or you can just drop in a URL notebook or you can just drop in a URL
    notebook or you can just drop in a URL

    something from GitHub. Um, and actually something from GitHub. Um, and actually
    something from GitHub. Um, and actually

    the um if you do modal.combook the um if you do modal.combook the um if you do
    modal.combook

    new and then put in a uh the name of a new and then put in a uh the name of a
    new and then put in a uh the name of a

    notebook. So here''s uh one there. Yeah. notebook. So here''s uh one there. Yeah.
    notebook. So here''s uh one there. Yeah.

    So this is this grabbed one from uh So this is this grabbed one from uh'
  concept_slugs: []
- idx: 69
  start_sec: 2935.28
  end_sec: 2972.0
  text: 'So this is this grabbed one from uh

    GitHub. It''s one of like Unslo''s model GitHub. It''s one of like Unslo''s model
    GitHub. It''s one of like Unslo''s model

    training notebooks. Um, that should open training notebooks. Um, that should open
    training notebooks. Um, that should open

    that notebook. that notebook. that notebook.

    That should open that notebook. Uh, oh, That should open that notebook. Uh, oh,
    That should open that notebook. Uh, oh,

    they might have sorry, they deleted that they might have sorry, they deleted that
    they might have sorry, they deleted that

    notebook. It''s gone. So, that''s why that notebook. It''s gone. So, that''s why
    that notebook. It''s gone. So, that''s why that

    didn''t work. Man, I should uh you got to didn''t work. Man, I should uh you got
    to didn''t work. Man, I should uh you got to

    be careful with demos, you know? You be careful with demos, you know? You be careful
    with demos, you know? You

    like so much so much stuff can go wrong. like so much so much stuff can go wrong.
    like so much so much stuff can go wrong.

    But anyway, so you put in you put in the But anyway, so you put in you put in
    the But anyway, so you put in you put in the

    URL there and you get a new notebook. URL there and you get a new notebook. URL
    there and you get a new notebook.

    Um, and yeah, and Kelly, if you wanted Um, and yeah, and Kelly, if you wanted
    Um, and yeah, and Kelly, if you wanted

    to like I can help you get hook you up to like I can help you get hook you up
    to like I can help you get hook you up

    with like a little badge, like a Moal with like a little badge, like a Moal with
    like a little badge, like a Moal

    notebook badge if you wanted to uh share notebook badge if you wanted to uh share
    notebook badge if you wanted to uh share

    those out with people. So, it''s just those out with people. So, it''s just those
    out with people. So, it''s just

    like one click on a little button and it like one click on a little button and
    it'
  concept_slugs: []
- idx: 70
  start_sec: 2972.0
  end_sec: 3018.64
  text: 'like one click on a little button and it

    turns into a modal notebook. turns into a modal notebook. turns into a modal notebook.

    >> Nice. Yeah, that that that could be >> Nice. Yeah, that that that could be
    >> Nice. Yeah, that that that could be

    nice. I can Yeah, I can add it to my the nice. I can Yeah, I can add it to my
    the nice. I can Yeah, I can add it to my the

    GitHub. I I''ll talk about this with you GitHub. I I''ll talk about this with
    you GitHub. I I''ll talk about this with you

    later. later. later.

    >> Yeah. Yeah. Sick. Um, >> Yeah. Yeah. Sick. Um, >> Yeah. Yeah. Sick. Um,

    cool. Uh, yeah. Any other? Yeah, happy cool. Uh, yeah. Any other? Yeah, happy
    cool. Uh, yeah. Any other? Yeah, happy

    to keep just keep answering questions to keep just keep answering questions to
    keep just keep answering questions

    instead of going through the, you know, instead of going through the, you know,
    instead of going through the, you know,

    sales pitch slides if any if anybody sales pitch slides if any if anybody sales
    pitch slides if any if anybody

    else has other questions. >> Uh, yeah, >> Uh, yeah,

    >> I have a question. So, you kind of >> I have a question. So, you kind of >>
    I have a question. So, you kind of

    mentioned the two extremes of training a mentioned the two extremes of training
    a mentioned the two extremes of training a

    model. One is you''re just experimenting model. One is you''re just experimenting
    model. One is you''re just experimenting

    in a Jupyter notebook and the other is in a Jupyter notebook and the other is
    in a Jupyter notebook and the other is

    you''re actually running all these you''re actually running all these you''re
    actually running all these

    parameter sweeps on um like a very parameter sweeps on um like a very parameter
    sweeps on um like a very

    compute heavy model. And so I''m compute heavy model. And so I''m compute heavy
    model. And so I''m

    wondering if you have any general advice wondering if you have any general advice
    wondering if you have any general advice

    for what to do in between that and and for what to do in between that and and'
  concept_slugs: []
- idx: 71
  start_sec: 3018.64
  end_sec: 3065.599
  text: 'for what to do in between that and and

    when do you kind of maybe know that it''s when do you kind of maybe know that
    it''s when do you kind of maybe know that it''s

    time to actually send it to a full scale time to actually send it to a full scale
    time to actually send it to a full scale

    kind of training uh pipeline so that kind of training uh pipeline so that kind
    of training uh pipeline so that

    you''re not kind of wasting resources and you''re not kind of wasting resources
    and you''re not kind of wasting resources and

    time and if modal maybe has any um time and if modal maybe has any um time and
    if modal maybe has any um

    uh kind of like plugins for for like uh kind of like plugins for for like uh kind
    of like plugins for for like

    building intuitions on that. building intuitions on that. building intuitions
    on that.

    >> Yeah. Yeah, it''s a good question. I >> Yeah. Yeah, it''s a good question.
    I >> Yeah. Yeah, it''s a good question. I

    think um think um think um

    yeah fundamentally like my goal and why yeah fundamentally like my goal and why
    yeah fundamentally like my goal and why

    I like you know fell in love with modal I like you know fell in love with modal
    I like you know fell in love with modal

    when I started using it is that I want when I started using it is that I want
    when I started using it is that I want

    to make it as like seamless as possible to make it as like seamless as possible
    to make it as like seamless as possible

    to switch between like like iterative to switch between like like iterative to
    switch between like like iterative

    experimentation and like a giant experimentation and like a giant experimentation
    and like a giant

    hyperparameter sweep and I so I like hyperparameter sweep and I so I like hyperparameter
    sweep and I so I like

    want like there there are so many things want like there there are so many things
    want like there there are so many things

    in the middle I want to be able to like in the middle I want to be able to like'
  concept_slugs: []
- idx: 72
  start_sec: 3065.599
  end_sec: 3108.16
  text: 'in the middle I want to be able to like

    switch between them really easily. So switch between them really easily. So switch
    between them really easily. So

    like this is kind of a like feels a like this is kind of a like feels a like this
    is kind of a like feels a

    little bit like a copout but like part little bit like a copout but like part
    little bit like a copout but like part

    of part of the answer is just like modal of part of the answer is just like modal
    of part of the answer is just like modal

    by trying to make it super like by trying to make it super like by trying to make
    it super like

    iteration loops super fast and like the iteration loops super fast and like the
    iteration loops super fast and like the

    same infrastructure both for your like same infrastructure both for your like
    same infrastructure both for your like

    scripts and your deployments and your scripts and your deployments and your scripts
    and your deployments and your

    hyperparameter sweeps just like slightly hyperparameter sweeps just like slightly
    hyperparameter sweeps just like slightly

    adjusting the way you hand manage the adjusting the way you hand manage the adjusting
    the way you hand manage the

    infrastructure like that um like that is infrastructure like that um like that
    is infrastructure like that um like that is

    trying to solve that exact problem trying to solve that exact problem trying to
    solve that exact problem

    you''re talking about. Um but I would say you''re talking about. Um but I would
    say you''re talking about. Um but I would say

    yeah in terms of like highlevel yeah in terms of like highlevel yeah in terms
    of like highlevel

    intuition for how to switch between like intuition for how to switch between like
    intuition for how to switch between like

    a super iterative mode and like a more a super iterative mode and like a more
    a super iterative mode and like a more

    like at scale automated like like at scale automated like like at scale automated
    like

    experimentation or exploration mode. I experimentation or exploration mode. I
    experimentation or exploration mode. I

    don''t have a great answer. I guess I don''t have a great answer. I guess I'
  concept_slugs: []
- idx: 73
  start_sec: 3108.16
  end_sec: 3154.71
  text: 'don''t have a great answer. I guess I

    would say that um would say that um would say that um

    it is it is it is

    as long as you have like good control as long as you have like good control as
    long as you have like good control

    over your tools so that you can switch over your tools so that you can switch
    over your tools so that you can switch

    back between like if you make something back between like if you make something
    back between like if you make something

    that''s more like automated or or or that''s more like automated or or or that''s
    more like automated or or or

    scales up that you can always still poke scales up that you can always still poke
    scales up that you can always still poke

    through and like you know and you know through and like you know and you know
    through and like you know and you know

    get into the guts and mess around with get into the guts and mess around with
    get into the guts and mess around with

    it like you can shell in you can attach it like you can shell in you can attach
    it like you can shell in you can attach

    a debugger whatever um then it''s a debugger whatever um then it''s a debugger
    whatever um then it''s

    generally a good idea to air on the side generally a good idea to air on the side
    generally a good idea to air on the side

    of of doing that sooner. Um, if you if of of doing that sooner. Um, if you if
    of of doing that sooner. Um, if you if

    it''s going to be difficult for you to be it''s going to be difficult for you
    to be it''s going to be difficult for you to be

    able to like once you attach the able to like once you attach the able to like
    once you attach the

    hyperparameter suits, once you attach hyperparameter suits, once you attach hyperparameter
    suits, once you attach

    like the extra compute, whatever it is like the extra compute, whatever it is
    like the extra compute, whatever it is

    that makes the larger scale thing that makes the larger scale thing that makes
    the larger scale thing

    different. If it be if that also makes'
  concept_slugs: []
- idx: 74
  start_sec: 3154.71
  end_sec: 3197.44
  text: 'different. If it be if that also makes different. If it be if that also makes

    it hard for you to like still experiment it hard for you to like still experiment
    it hard for you to like still experiment

    and still like you know get an and still like you know get an and still like you
    know get an

    interactive attachment to the work that interactive attachment to the work that
    interactive attachment to the work that

    you''re doing then you want to like delay you''re doing then you want to like
    delay you''re doing then you want to like delay

    it for as long as possible actually. U it for as long as possible actually. U
    it for as long as possible actually. U

    so that''s I don''t know hopefully that''s so that''s I don''t know hopefully
    that''s so that''s I don''t know hopefully that''s

    helpful. helpful. helpful.

    >> Yeah thank you. >> Yeah thank you. >> Yeah thank you.

    >> Uh I actually have like a like another >> Uh I actually have like a like another
    >> Uh I actually have like a like another

    followup on this. So basically the the followup on this. So basically the the
    followup on this. So basically the the

    way that I develop the homework was sort way that I develop the homework was sort
    way that I develop the homework was sort

    of just like of just like of just like

    >> um like basically I I''ll try to like do >> um like basically I I''ll try to
    like do >> um like basically I I''ll try to like do

    some smaller scale experiment but every some smaller scale experiment but every
    some smaller scale experiment but every

    time I do it I''ll try to just like send time I do it I''ll try to just like send
    time I do it I''ll try to just like send

    like a so I''ll just like send a modal like a so I''ll just like send a modal
    like a so I''ll just like send a modal

    job but sometimes maybe this is like not job but sometimes maybe this is like
    not job but sometimes maybe this is like not

    the best way for debugging. So I was the best way for debugging. So I was'
  concept_slugs: []
- idx: 75
  start_sec: 3197.44
  end_sec: 3248.069
  text: 'the best way for debugging. So I was

    wondering like is modal shell like the wondering like is modal shell like the
    wondering like is modal shell like the

    best way for people to to debug? If you best way for people to to debug? If you
    best way for people to to debug? If you

    like say you run things and then you like say you run things and then you like
    say you run things and then you

    make changes and do [snorts] you need to make changes and do [snorts] you need
    to make changes and do [snorts] you need to

    like rerun the app or like so what I like rerun the app or like so what I like
    rerun the app or like so what I

    guess the question is that what is the guess the question is that what is the
    guess the question is that what is the

    best way to debug with model? best way to debug with model? best way to debug
    with model?

    >> Yeah. So there''s a couple different ways >> Yeah. So there''s a couple different
    ways >> Yeah. So there''s a couple different ways

    to do it. I think I can just do this. U to do it. I think I can just do this.
    U to do it. I think I can just do this. U

    let''s see again we''re like uh you know let''s see again we''re like uh you know
    let''s see again we''re like uh you know

    running close to the sun but let''s do running close to the sun but let''s do
    running close to the sun but let''s do

    modal run d-inact modal run d-inact modal run d-inact

    if actually no let''s just do dash i if actually no let''s just do dash i if actually
    no let''s just do dash i

    pretty confident about that 01 getting pretty confident about that 01 getting
    pretty confident about that 01 getting

    started inference.py Pi. So I should be started inference.py Pi. So I should be
    started inference.py Pi. So I should be

    able to This should drop me into like a able to This should drop me into like
    a able to This should drop me into like a

    debugger inside of this function. Let''s debugger inside of this function. Let''s
    debugger inside of this function. Let''s

    see what happens.'
  concept_slugs: []
- idx: 76
  start_sec: 3248.069
  end_sec: 3295.2
  text: 'see what happens. see what happens.

    Um, all right. Yeah, it takes a second Um, all right. Yeah, it takes a second
    Um, all right. Yeah, it takes a second

    to load. Okay, there we go. If prompt is to load. Okay, there we go. If prompt
    is to load. Okay, there we go. If prompt is

    none. So yeah, so pipeline should exist. none. So yeah, so pipeline should exist.
    none. So yeah, so pipeline should exist.

    Yeah, and then yeah, I can import Yeah, and then yeah, I can import Yeah, and
    then yeah, I can import

    transformers. transformers. transformers.

    So yeah, so you can still get some of So yeah, so you can still get some of So
    yeah, so you can still get some of

    this like um this like um this like um

    uh you can still get like a pretty good uh you can still get like a pretty good
    uh you can still get like a pretty good

    debugging experience on modal if you uh debugging experience on modal if you uh
    debugging experience on modal if you uh

    know about some of these like advanced know about some of these like advanced
    know about some of these like advanced

    features. So we do have a page in the features. So we do have a page in the features.
    So we do have a page in the

    docs modal docs uh debugging developing docs modal docs uh debugging developing
    docs modal docs uh debugging developing

    and debugging on modal. So this uh sort and debugging on modal. So this uh sort
    and debugging on modal. So this uh sort

    of explains a bunch of this of explains a bunch of this of explains a bunch of
    this

    interactivity stuff. Um and yeah the interactivity stuff. Um and yeah the interactivity
    stuff. Um and yeah the

    breakpoint you can also get this is a breakpoint you can also get this is a breakpoint
    you can also get this is a

    fun one like get an IPython ripple fun one like get an IPython ripple fun one
    like get an IPython ripple

    inside of a function. Um and then you inside of a function. Um and then you inside
    of a function. Um and then you

    can also uh like I showed you modal can also uh like I showed you modal'
  concept_slugs: []
- idx: 77
  start_sec: 3295.2
  end_sec: 3346.24
  text: 'can also uh like I showed you modal

    shell. You can also modal shell by shell. You can also modal shell by shell. You
    can also modal shell by

    default if you like pointed at um default if you like pointed at um default if
    you like pointed at um

    something like this file modal shell something like this file modal shell something
    like this file modal shell

    will like spin up a new replica. But if will like spin up a new replica. But if
    will like spin up a new replica. But if

    you have running code like running you have running code like running you have
    running code like running

    containers on modal you can also modal containers on modal you can also modal
    containers on modal you can also modal

    shell into the running container and shell into the running container and shell
    into the running container and

    like debug a like actually running like debug a like actually running like debug
    a like actually running

    container. Um, yeah. So there''s, yeah, container. Um, yeah. So there''s, yeah,
    container. Um, yeah. So there''s, yeah,

    anyway, so there''s and and like live anyway, so there''s and and like live anyway,
    so there''s and and like live

    profiling, so you can actually watch profiling, so you can actually watch profiling,
    so you can actually watch

    your, you know, instruction pointer move your, you know, instruction pointer move
    your, you know, instruction pointer move

    around in your code. That''s also good around in your code. That''s also good
    around in your code. That''s also good

    for the sort of like debugging. Um, for the sort of like debugging. Um, for the
    sort of like debugging. Um,

    yeah. Uh, so couple different options yeah. Uh, so couple different options yeah.
    Uh, so couple different options

    there. Um, there. Um, there. Um,

    yeah, and then you have the notebooks as yeah, and then you have the notebooks
    as yeah, and then you have the notebooks as

    well for sort of like the at the very well for sort of like the at the very well
    for sort of like the at the very

    like highest levels of iteration. like highest levels of iteration. like highest
    levels of iteration.

    I have a question about uh your process I have a question about uh your process'
  concept_slugs: []
- idx: 78
  start_sec: 3346.24
  end_sec: 3388.48
  text: 'I have a question about uh your process

    earlier. You said you sample uh like you earlier. You said you sample uh like
    you earlier. You said you sample uh like you

    had tens of thousands of photos and then had tens of thousands of photos and then
    had tens of thousands of photos and then

    you sample like 1,800 of them and you sample like 1,800 of them and you sample
    like 1,800 of them and

    [clears throat] you went on to look at [clears throat] you went on to look at
    [clears throat] you went on to look at

    every single one and then figure out every single one and then figure out every
    single one and then figure out

    your process from there. I was wondering your process from there. I was wondering
    your process from there. I was wondering

    if it was possible um on the newer side, if it was possible um on the newer side,
    if it was possible um on the newer side,

    but like if you could just run like some but like if you could just run like some
    but like if you could just run like some

    type of clustering algorithm or type of clustering algorithm or type of clustering
    algorithm or

    something to at least get your data into something to at least get your data into
    something to at least get your data into

    buckets and then sample of each bucket buckets and then sample of each bucket
    buckets and then sample of each bucket

    or is that a naive approach? or is that a naive approach? or is that a naive approach?

    >> Yeah. Uh well, I think I think it''s the >> Yeah. Uh well, I think I think
    it''s the >> Yeah. Uh well, I think I think it''s the

    opposite. I think it''s an overly opposite. I think it''s an overly opposite.
    I think it''s an overly

    sophisticated approach which is like I sophisticated approach which is like I
    sophisticated approach which is like I

    think like yeah if you had like really think like yeah if you had like really
    think like yeah if you had like really

    large amounts of data and you were large amounts of data and you were large amounts
    of data and you were

    worried about doing fair sampling then worried about doing fair sampling then'
  concept_slugs: []
- idx: 79
  start_sec: 3388.48
  end_sec: 3427.44
  text: 'worried about doing fair sampling then

    yeah you would want to do like more yeah you would want to do like more yeah you
    would want to do like more

    sophisticated ML at the at the start. Um sophisticated ML at the at the start.
    Um sophisticated ML at the at the start. Um

    and especially like if you have more and especially like if you have more and
    especially like if you have more

    data then maybe you have more engineers data then maybe you have more engineers
    data then maybe you have more engineers

    and you have more bandwidth to do that and you have more bandwidth to do that
    and you have more bandwidth to do that

    sort of thing. Um but for a project like sort of thing. Um but for a project like
    sort of thing. Um but for a project like

    this one you kind of just want to like this one you kind of just want to like
    this one you kind of just want to like

    you know you do this before you do any you know you do this before you do any
    you know you do this before you do any

    like sort of clustering. You want to like sort of clustering. You want to like
    sort of clustering. You want to

    look at the data as raw as possible look at the data as raw as possible look at
    the data as raw as possible

    before you like dive in and uh before before you like dive in and uh before before
    you like dive in and uh before

    you start like process passing it you start like process passing it you start
    like process passing it

    through machines and filters uh before through machines and filters uh before
    through machines and filters uh before

    they get to you. Uh so yeah they get to you. Uh so yeah they get to you. Uh so
    yeah

    >> so kind of like a proof of concept like >> so kind of like a proof of concept
    like >> so kind of like a proof of concept like

    get it done. get it done. get it done.

    >> Yeah. Yeah. And like sort of the proof >> Yeah. Yeah. And like sort of the
    proof'
  concept_slugs: []
- idx: 80
  start_sec: 3427.44
  end_sec: 3470.549
  text: '>> Yeah. Yeah. And like sort of the proof

    of during the like sort of proof of of during the like sort of proof of of during
    the like sort of proof of

    concept phases in ML you want to spend concept phases in ML you want to spend
    concept phases in ML you want to spend

    time with the raw data as raw as time with the raw data as raw as time with the
    raw data as raw as

    possible. I also think it''s like it''s possible. I also think it''s like it''s
    possible. I also think it''s like it''s

    good to go back to the raw data as often good to go back to the raw data as often
    good to go back to the raw data as often

    as possible to sort of like make sure as possible to sort of like make sure as
    possible to sort of like make sure

    you aren''t getting fooled by all the you aren''t getting fooled by all the you
    aren''t getting fooled by all the

    other systems you''ve put in place like other systems you''ve put in place like
    other systems you''ve put in place like

    in between you and and the real world. in between you and and the real world.
    in between you and and the real world.

    But um but yeah, but clustering is like But um but yeah, but clustering is like
    But um but yeah, but clustering is like

    an excellent tool for discovering like an excellent tool for discovering like
    an excellent tool for discovering like

    struct during the during earlier phases. struct during the during earlier phases.
    struct during the during earlier phases.

    It can also be useful for discovering It can also be useful for discovering It
    can also be useful for discovering

    structure that you don''t know to like structure that you don''t know to like
    structure that you don''t know to like

    use unsupervised ML methods to sort of use unsupervised ML methods to sort of
    use unsupervised ML methods to sort of

    like show you that there''s something in like show you that there''s something
    in like show you that there''s something in

    your data that you wouldn''t find your data that you wouldn''t find your data
    that you wouldn''t find

    otherwise. otherwise. otherwise.

    Okay, thank you.'
  concept_slugs: []
- idx: 81
  start_sec: 3473.349
  end_sec: 3506.789
  text: '>> Um, cool. All right, with uh we we got >> Um, cool. All right, with uh
    we we got

    about like 10 minutes left, so I''ll go a about like 10 minutes left, so I''ll
    go a about like 10 minutes left, so I''ll go a

    little bit faster. I''ll say like one little bit faster. I''ll say like one little
    bit faster. I''ll say like one

    thing is yeah, modal we do do a lot of thing is yeah, modal we do do a lot of
    thing is yeah, modal we do do a lot of

    infrastructure work. We like to talk infrastructure work. We like to talk infrastructure
    work. We like to talk

    about the work that we do because um you about the work that we do because um
    you about the work that we do because um you

    know we think yeah it''s makes it clear know we think yeah it''s makes it clear
    know we think yeah it''s makes it clear

    why it''s useful to use a tool like modal why it''s useful to use a tool like
    modal why it''s useful to use a tool like modal

    because building it is like kind of hard because building it is like kind of hard
    because building it is like kind of hard

    if you wanted to try and make all this if you wanted to try and make all this
    if you wanted to try and make all this

    container infrastructure yourself. Um so container infrastructure yourself. Um
    so container infrastructure yourself. Um so

    yeah check out we''ve got a couple of yeah check out we''ve got a couple of yeah
    check out we''ve got a couple of

    things from our founder and from our things from our founder and from our things
    from our founder and from our

    engineers that uh sort of talk about all engineers that uh sort of talk about
    all engineers that uh sort of talk about all

    the things that make this thing work. Um the things that make this thing work.
    Um the things that make this thing work. Um

    I will kind of skip over this like list I will kind of skip over this like list
    I will kind of skip over this like list

    of features. I''ll just say like we have'
  concept_slugs: []
- idx: 82
  start_sec: 3506.789
  end_sec: 3555.599
  text: 'of features. I''ll just say like we have of features. I''ll just say like
    we have

    things that help you do storage and things that help you do storage and things
    that help you do storage and

    communication whether that''s like communication whether that''s like communication
    whether that''s like

    distributed file storage with volumes distributed file storage with volumes distributed
    file storage with volumes

    dictionaries and cues for sort of more dictionaries and cues for sort of more
    dictionaries and cues for sort of more

    like operational communication between like operational communication between
    like operational communication between

    your like many concurrent or or um your like many concurrent or or um your like
    many concurrent or or um

    parallel replicas that you''re running. parallel replicas that you''re running.
    parallel replicas that you''re running.

    Um, of course, you know, we have Um, of course, you know, we have Um, of course,
    you know, we have

    functions. We have sandboxes uh for functions. We have sandboxes uh for functions.
    We have sandboxes uh for

    doing AI code. Probably not something doing AI code. Probably not something doing
    AI code. Probably not something

    that matters that matters that matters

    as much if you''re focused on media as much if you''re focused on media as much
    if you''re focused on media

    generation instead of uh text generation instead of uh text generation instead
    of uh text

    generation. Um and uh maybe maybe generation. Um and uh maybe maybe generation.
    Um and uh maybe maybe

    critically for folks who are more critically for folks who are more critically
    for folks who are more

    focused on the like model training side, focused on the like model training side,
    focused on the like model training side,

    modal makes it really easy to set up modal makes it really easy to set up modal
    makes it really easy to set up

    like web endpoints and web servers, even like web endpoints and web servers, even
    like web endpoints and web servers, even

    if you know just you know in Python if you know just you know in Python if you
    know just you know in Python

    without having to know a ton of stuff without having to know a ton of stuff without
    having to know a ton of stuff

    about u like the HTTP stack. Um, so you about u like the HTTP stack. Um, so you'
  concept_slugs: []
- idx: 83
  start_sec: 3555.599
  end_sec: 3598.4
  text: 'about u like the HTTP stack. Um, so you

    can take something like Streamlit or can take something like Streamlit or can
    take something like Streamlit or

    Graddio and serve it on modal and then Graddio and serve it on modal and then
    Graddio and serve it on modal and then

    actually have something that you can actually have something that you can actually
    have something that you can

    like look at on your phone, share with like look at on your phone, share with
    like look at on your phone, share with

    like your friends or or like you know in like your friends or or like you know
    in like your friends or or like you know in

    the business world share with the business world share with the business world
    share with

    stakeholders. Uh, and so those that''s stakeholders. Uh, and so those that''s
    stakeholders. Uh, and so those that''s

    like kind of a useful set of features like kind of a useful set of features like
    kind of a useful set of features

    for y''all. Um, so yeah, we talked about for y''all. Um, so yeah, we talked about
    for y''all. Um, so yeah, we talked about

    all the different features of the all the different features of the all the different
    features of the

    dashboard already. Uh, yeah, sandboxes. dashboard already. Uh, yeah, sandboxes.
    dashboard already. Uh, yeah, sandboxes.

    This all comes from this like large This all comes from this like large This all
    comes from this like large

    scale LLM code evaluation example that scale LLM code evaluation example that
    scale LLM code evaluation example that

    you can find if you look at the slides. you can find if you look at the slides.
    you can find if you look at the slides.

    Um yeah we got uh for training these uh Um yeah we got uh for training these uh
    Um yeah we got uh for training these uh

    volumes are going to be super useful for volumes are going to be super useful
    for volumes are going to be super useful for

    storing data and for storing weights. Um storing data and for storing weights.
    Um storing data and for storing weights. Um

    then you store them in you store the then you store them in you store the'
  concept_slugs: []
- idx: 84
  start_sec: 3598.4
  end_sec: 3635.52
  text: 'then you store them in you store the

    weights in one of these uh distributed weights in one of these uh distributed
    weights in one of these uh distributed

    volumes and then you can actually while volumes and then you can actually while
    volumes and then you can actually while

    if you set up your MLOps sort of stuff if you set up your MLOps sort of stuff
    if you set up your MLOps sort of stuff

    on modal right you can save weights to a on modal right you can save weights to
    a on modal right you can save weights to a

    volume while you''re training and then volume while you''re training and then
    volume while you''re training and then

    also like deploy a grado app that can also like deploy a grado app that can also
    like deploy a grado app that can

    look at that same volume and then look look at that same volume and then look
    look at that same volume and then look

    at the weights like halfway through your at the weights like halfway through your
    at the weights like halfway through your

    training run you can go and play around training run you can go and play around
    training run you can go and play around

    with the a model and see whether that with the a model and see whether that with
    the a model and see whether that

    training run is working or not. Um, so training run is working or not. Um, so
    training run is working or not. Um, so

    to Kelly''s point about like being able to Kelly''s point about like being able
    to Kelly''s point about like being able

    to quickly figure out whether to quickly figure out whether to quickly figure
    out whether

    something''s busted, like sending a few something''s busted, like sending a few
    something''s busted, like sending a few

    prompts is like often uh and then like prompts is like often uh and then like
    prompts is like often uh and then like

    interacting back and forth. Like you interacting back and forth. Like you interacting
    back and forth. Like you

    send a prompt, it looks a little bit send a prompt, it looks a little bit send
    a prompt, it looks a little bit

    funny, you try a slightly different funny, you try a slightly different'
  concept_slugs: []
- idx: 85
  start_sec: 3635.52
  end_sec: 3680.88
  text: 'funny, you try a slightly different

    version, that can be better than any version, that can be better than any version,
    that can be better than any

    sort of fixed eval that you can write sort of fixed eval that you can write sort
    of fixed eval that you can write

    down. Um, so that sort of interactivity down. Um, so that sort of interactivity
    down. Um, so that sort of interactivity

    is nice. Um, yeah, and you know, serving is nice. Um, yeah, and you know, serving
    is nice. Um, yeah, and you know, serving

    your own like fast API endpoints or or your own like fast API endpoints or or
    your own like fast API endpoints or or

    gradio apps is is great. So, um, my gradio apps is is great. So, um, my gradio
    apps is is great. So, um, my

    recommendation if you want to try out recommendation if you want to try out recommendation
    if you want to try out

    modal, I would recommend getting started modal, I would recommend getting started
    modal, I would recommend getting started

    with one of our examples. Um, like some with one of our examples. Um, like some
    with one of our examples. Um, like some

    of the most important ones for you all, of the most important ones for you all,
    of the most important ones for you all,

    this this one right here is like this this one right here is like this this one
    right here is like

    fine-tuning [clears throat] fine-tuning [clears throat] fine-tuning [clears throat]

    flux on a picture pictures of your pet flux on a picture pictures of your pet
    flux on a picture pictures of your pet

    so that you can then generate like, you so that you can then generate like, you
    so that you can then generate like, you

    know, arbitrary little fun generations know, arbitrary little fun generations
    know, arbitrary little fun generations

    of your of your pet on the moon or of your of your pet on the moon or of your
    of your pet on the moon or

    whatever. Um, some stuff about serving whatever. Um, some stuff about serving
    whatever. Um, some stuff about serving

    here inference optimizations. Those are here inference optimizations. Those are
    here inference optimizations. Those are

    probably less important for training. Um probably less important for training.
    Um'
  concept_slugs: []
- idx: 86
  start_sec: 3680.88
  end_sec: 3729.52
  text: 'probably less important for training. Um

    maybe actually I''ll just go to this page maybe actually I''ll just go to this
    page maybe actually I''ll just go to this page

    and like kind of pull up some highlights and like kind of pull up some highlights
    and like kind of pull up some highlights

    so you can see them so you can see them so you can see them

    slightly. Zoom back out. A lot of stuff slightly. Zoom back out. A lot of stuff
    slightly. Zoom back out. A lot of stuff

    about LM these days because people love about LM these days because people love
    about LM these days because people love

    LMS. Uh but let''s go to images video. LMS. Uh but let''s go to images video.
    LMS. Uh but let''s go to images video.

    Yeah, couple different ways to serve Yeah, couple different ways to serve Yeah,
    couple different ways to serve

    diffusion models. Oh yeah, if you want diffusion models. Oh yeah, if you want
    diffusion models. Oh yeah, if you want

    to do some cool real time stuff um which to do some cool real time stuff um which
    to do some cool real time stuff um which

    is maybe something to do for your is maybe something to do for your is maybe something
    to do for your

    project in the class during the project in the class during the project in the
    class during the

    inference step, we have some stuff about inference step, we have some stuff about
    inference step, we have some stuff about

    how to do WebRTC how to do WebRTC how to do WebRTC

    um which will definitely impress your uh um which will definitely impress your
    uh um which will definitely impress your uh

    your professors and and your friends your professors and and your friends your
    professors and and your friends

    even maybe uh then maybe the other piece even maybe uh then maybe the other piece
    even maybe uh then maybe the other piece

    is training. What do I have here? I is training. What do I have here? I is training.
    What do I have here? I

    don''t have a great training like MLOps don''t have a great training like MLOps
    don''t have a great training like MLOps

    training example with um this this uh training example with um this this uh'
  concept_slugs: []
- idx: 87
  start_sec: 3729.52
  end_sec: 3774.079
  text: 'training example with um this this uh

    pet art fine-tune is like a very small pet art fine-tune is like a very small
    pet art fine-tune is like a very small

    scale training but this one here shows scale training but this one here shows
    scale training but this one here shows

    uh how to train a language model from uh how to train a language model from uh
    how to train a language model from

    scratch and it includes some of the the scratch and it includes some of the the
    scratch and it includes some of the the

    thing where you can like try a model out thing where you can like try a model
    out thing where you can like try a model out

    partway through training that''s what partway through training that''s what partway
    through training that''s what

    this um radio UI here uh shows like pick this um radio UI here uh shows like pick
    this um radio UI here uh shows like pick

    a model version and then interact with a model version and then interact with
    a model version and then interact with

    it um and uh Yeah, with hyperparameter it um and uh Yeah, with hyperparameter
    it um and uh Yeah, with hyperparameter

    sweeps, with tensorboard for experiment sweeps, with tensorboard for experiment
    sweeps, with tensorboard for experiment

    logging, all that stuff. So, you know, logging, all that stuff. So, you know,
    logging, all that stuff. So, you know,

    obviously you''re not going to be obviously you''re not going to be obviously
    you''re not going to be

    training a transformer language model in training a transformer language model
    in training a transformer language model in

    this course, but it''s probably a good um this course, but it''s probably a good
    um this course, but it''s probably a good um

    you can get some good ideas, high level you can get some good ideas, high level
    you can get some good ideas, high level

    ideas from that. ideas from that. ideas from that.

    Um, yeah, one thing I will say is we we Um, yeah, one thing I will say is we we
    Um, yeah, one thing I will say is we we

    put a lot of effort into ensuring that put a lot of effort into ensuring that'
  concept_slugs: []
- idx: 88
  start_sec: 3774.079
  end_sec: 3811.68
  text: 'put a lot of effort into ensuring that

    these examples are actually good. I these examples are actually good. I these
    examples are actually good. I

    think a lot of people have I hate really think a lot of people have I hate really
    think a lot of people have I hate really

    bad docs. I feel victimized by all the bad docs. I feel victimized by all the
    bad docs. I feel victimized by all the

    poor documentation people have out there poor documentation people have out there
    poor documentation people have out there

    for their software. So we make sure for their software. So we make sure for their
    software. So we make sure

    these the we have an automated system these the we have an automated system these
    the we have an automated system

    for running this like multiple times a for running this like multiple times a
    for running this like multiple times a

    day and tracking rates of failure and day and tracking rates of failure and day
    and tracking rates of failure and

    like uh and ensuring that things work. like uh and ensuring that things work.
    like uh and ensuring that things work.

    So if you notice any of these examples So if you notice any of these examples
    So if you notice any of these examples

    don''t work. Um they fel and they fell don''t work. Um they fel and they fell
    don''t work. Um they fel and they fell

    through our uh our testing at somehow through our uh our testing at somehow through
    our uh our testing at somehow

    please let me know so we can fix it. But please let me know so we can fix it.
    But please let me know so we can fix it. But

    you should have we have about two nines you should have we have about two nines
    you should have we have about two nines

    of reliability on these examples. Uh so of reliability on these examples. Uh so
    of reliability on these examples. Uh so

    uh and that''s a lot better than I''d say uh and that''s a lot better than I''d
    say uh and that''s a lot better than I''d say

    it seems like most people have about 50% it seems like most people have about
    50%'
  concept_slugs: []
- idx: 89
  start_sec: 3811.68
  end_sec: 3861.52
  text: 'it seems like most people have about 50%

    reliability on the code in their reliability on the code in their reliability
    on the code in their

    documentation. documentation. documentation.

    >> Cool. Uh yeah, we still have >> Cool. Uh yeah, we still have >> Cool. Uh yeah,
    we still have

    [clears throat] maybe five minutes, [clears throat] maybe five minutes, [clears
    throat] maybe five minutes,

    right? So happy to answer any last right? So happy to answer any last right? So
    happy to answer any last

    questions people have really about about questions people have really about about
    questions people have really about about

    uh anything. >> Um I Yeah, go ahead. No, no, no. Oh, I I >> Um I Yeah, go ahead.
    No, no, no. Oh, I I

    mean I I just wanted to say that like mean I I just wanted to say that like mean
    I I just wanted to say that like

    the starter code that I gave you guys the starter code that I gave you guys the
    starter code that I gave you guys

    already have like the modal app thing already have like the modal app thing already
    have like the modal app thing

    built in and it should it should just built in and it should it should just built
    in and it should it should just

    work I think. Um but if if it doesn''t, work I think. Um but if if it doesn''t,
    work I think. Um but if if it doesn''t,

    I''m pretty sure you can fix it with all I''m pretty sure you can fix it with
    all I''m pretty sure you can fix it with all

    the AI tools that I you''re allowed to the AI tools that I you''re allowed to
    the AI tools that I you''re allowed to

    use. So um yeah, I just tried it out. use. So um yeah, I just tried it out. use.
    So um yeah, I just tried it out.

    It''s like pretty fun. Yeah. Go ahead. Uh It''s like pretty fun. Yeah. Go ahead.
    Uh It''s like pretty fun. Yeah. Go ahead. Uh

    >> I actually have a question about the QR >> I actually have a question about
    the QR >> I actually have a question about the QR

    code project. Mhm. code project. Mhm.'
  concept_slugs: []
- idx: 90
  start_sec: 3861.52
  end_sec: 3899.19
  text: 'code project. Mhm.

    >> Um I''m just curious if you found a point >> Um I''m just curious if you found
    a point >> Um I''m just curious if you found a point

    where the aesthetics are so good that where the aesthetics are so good that where
    the aesthetics are so good that

    people don''t recognize it''s a QR code people don''t recognize it''s a QR code
    people don''t recognize it''s a QR code

    anymore and then uh don''t know that they anymore and then uh don''t know that
    they anymore and then uh don''t know that they

    should scan it. If you''re just should scan it. If you''re just should scan it.
    If you''re just

    experimenting with that. experimenting with that. experimenting with that.

    >> Yeah. Yeah. I think it it depends on the >> Yeah. Yeah. I think it it depends
    on the >> Yeah. Yeah. I think it it depends on the

    application, right? Um so the way that I application, right? Um so the way that
    I application, right? Um so the way that I

    tend to use them is kind of the way that tend to use them is kind of the way that
    tend to use them is kind of the way that

    you''ve seen them in this um uh in these you''ve seen them in this um uh in these
    you''ve seen them in this um uh in these

    slides where it''s like very obvious. Uh, slides where it''s like very obvious.
    Uh, slides where it''s like very obvious. Uh,

    I guess the other way that I use them is I guess the other way that I use them
    is I guess the other way that I use them is

    that I''ve printed them out as stickers that I''ve printed them out as stickers
    that I''ve printed them out as stickers

    and like hung them up in bathrooms and and like hung them up in bathrooms and
    and like hung them up in bathrooms and

    bars. Um, and that''s maybe you want bars. Um, and that''s maybe you want bars.
    Um, and that''s maybe you want

    people to kind of figure it out um on people to kind of figure it out um on people
    to kind of figure it out um on

    their own. But often I think a lot of'
  concept_slugs: []
- idx: 91
  start_sec: 3899.19
  end_sec: 3951.76
  text: 'their own. But often I think a lot of their own. But often I think a lot
    of

    times with QR codes there''s like other times with QR codes there''s like other
    times with QR codes there''s like other

    sort of signifiers of the affordance of sort of signifiers of the affordance of
    sort of signifiers of the affordance of

    scannability. Um, but yeah, I would say scannability. Um, but yeah, I would say
    scannability. Um, but yeah, I would say

    most of the time the um the aesthetics most of the time the um the aesthetics
    most of the time the um the aesthetics

    are just not quite there where you''d are just not quite there where you''d are
    just not quite there where you''d

    have to worry about about it being have to worry about about it being have to
    worry about about it being

    totally nonobvious. It''s not like uh totally nonobvious. It''s not like uh totally
    nonobvious. It''s not like uh

    it''s not like steganographic where it''s it''s not like steganographic where
    it''s it''s not like steganographic where it''s

    like actually hidden from anybody who like actually hidden from anybody who like
    actually hidden from anybody who

    doesn''t realize that it''s a QR code. Um doesn''t realize that it''s a QR code.
    Um doesn''t realize that it''s a QR code. Um

    yeah. >> All right. Any other [clears throat] >> All right. Any other [clears
    throat]

    >> Oh, yeah. Go ahead. You >> Oh, yeah. Go ahead. You >> Oh, yeah. Go ahead. You

    >> you mentioned you tried to make your >> you mentioned you tried to make your
    >> you mentioned you tried to make your

    starter code work with the modal thing. starter code work with the modal thing.
    starter code work with the modal thing.

    Yeah. Yeah. Yeah.

    >> Can I essentially just create the modal >> Can I essentially just create the
    modal >> Can I essentially just create the modal

    app and then drop in the cloned app and then drop in the cloned app and then drop
    in the cloned

    get environment. Will it work with the get environment. Will it work with the
    get environment. Will it work with the

    app? How''s that kind of all? app? How''s that kind of all? app? How''s that kind
    of all?

    >> Um, >> Um,'
  concept_slugs: []
- idx: 92
  start_sec: 3951.76
  end_sec: 3993.68
  text: '>> Um,

    you mean in general or you mean like you mean in general or you mean like you
    mean in general or you mean like

    >> in general and and for this time? >> in general and and for this time? >> in
    general and and for this time?

    >> Oh, uh, I I don''t know how to answer >> Oh, uh, I I don''t know how to answer
    >> Oh, uh, I I don''t know how to answer

    that in general, but for this time, that in general, but for this time, that in
    general, but for this time,

    basically, uh, what I did in the modal basically, uh, what I did in the modal
    basically, uh, what I did in the modal

    app is that like it just like calls a app is that like it just like calls a app
    is that like it just like calls a

    sub um, process that like uses your sub um, process that like uses your sub um,
    process that like uses your

    train py or sample. Or eval py. So train py or sample. Or eval py. So train py
    or sample. Or eval py. So

    essentially, you probably don''t even essentially, you probably don''t even essentially,
    you probably don''t even

    need to touch the model car. you can need to touch the model car. you can need
    to touch the model car. you can

    just do motor run something. You just just do motor run something. You just just
    do motor run something. You just

    select your thing. But in a lot of the select your thing. But in a lot of the
    select your thing. But in a lot of the

    times maybe you want to add other times maybe you want to add other times maybe
    you want to add other

    functions. So we I only have like the functions. So we I only have like the functions.
    So we I only have like the

    most like basic ones that you you may most like basic ones that you you may most
    like basic ones that you you may

    want to use. But like if you want to want to use. But like if you want to want
    to use. But like if you want to

    like do other experiments other than the like do other experiments other than
    the'
  concept_slugs: []
- idx: 93
  start_sec: 3993.68
  end_sec: 4036.319
  text: 'like do other experiments other than the

    ones that I set up for you, then you''ll ones that I set up for you, then you''ll
    ones that I set up for you, then you''ll

    have to write your own function kind of. have to write your own function kind
    of. have to write your own function kind of.

    But then just like very easy to do. Um I But then just like very easy to do. Um
    I But then just like very easy to do. Um I

    don''t in general um I don''t know how how don''t in general um I don''t know
    how how don''t in general um I don''t know how how

    how in general um things works. So maybe how in general um things works. So maybe
    how in general um things works. So maybe

    Charles you can answer that part. Charles you can answer that part. Charles you
    can answer that part.

    >> Uh yeah hard to say without looking at >> Uh yeah hard to say without looking
    at >> Uh yeah hard to say without looking at

    the the code that you have but yeah it the the code that you have but yeah it
    the the code that you have but yeah it

    sounds like um yeah if you it''s sounds like um yeah if you it''s sounds like
    um yeah if you it''s

    something you just trigger with modal something you just trigger with modal something
    you just trigger with modal

    run then you could focus on the like run then you could focus on the like run
    then you could focus on the like

    separate script. Um, I just wanted to separate script. Um, I just wanted to separate
    script. Um, I just wanted to

    maybe jump on a point that you made maybe jump on a point that you made maybe
    jump on a point that you made

    earlier, which is like um, uh, using the earlier, which is like um, uh, using
    the earlier, which is like um, uh, using the

    various AI tools to be able to do this various AI tools to be able to do this
    various AI tools to be able to do this

    faster. So, one is we have an LLM.ext. faster. So, one is we have an LLM.ext.'
  concept_slugs: []
- idx: 94
  start_sec: 4036.319
  end_sec: 4077.19
  text: 'faster. So, one is we have an LLM.ext.

    This gets updated every time we update This gets updated every time we update
    This gets updated every time we update

    our docs um, and like has a bunch of our docs um, and like has a bunch of our
    docs um, and like has a bunch of

    links in it to doc pages. And if you go links in it to doc pages. And if you go
    links in it to doc pages. And if you go

    to any of these doc pages, like this one to any of these doc pages, like this
    one to any of these doc pages, like this one

    on building container images, you can on building container images, you can on
    building container images, you can

    get a clean markdown version of the page get a clean markdown version of the page
    get a clean markdown version of the page

    with this button and you can drop that with this button and you can drop that
    with this button and you can drop that

    into an agent''s context. Um, and then we into an agent''s context. Um, and then
    we into an agent''s context. Um, and then we

    also have some tips and tricks. Uh, this also have some tips and tricks. Uh, this
    also have some tips and tricks. Uh, this

    page has like basically your sort of page has like basically your sort of page
    has like basically your sort of

    like claw.md type thing. Uh, this is like claw.md type thing. Uh, this is like
    claw.md type thing. Uh, this is

    just like a nice starter on this page. just like a nice starter on this page.
    just like a nice starter on this page.

    So, [clears throat] just a couple of So, [clears throat] just a couple of So,
    [clears throat] just a couple of

    things that we have that uh should help things that we have that uh should help
    things that we have that uh should help

    you get going a little bit faster. Um you get going a little bit faster. Um you
    get going a little bit faster. Um

    the examples also work pretty well for the examples also work pretty well for
    the examples also work pretty well for

    that. That''s um I developed the examples'
  concept_slugs: []
- idx: 95
  start_sec: 4077.19
  end_sec: 4126.839
  text: 'that. That''s um I developed the examples that. That''s um I developed the
    examples

    in part by copying and pasting examples in part by copying and pasting examples
    in part by copying and pasting examples

    into cloud code and then having it uh into cloud code and then having it uh into
    cloud code and then having it uh

    yeah um update them and and make new yeah um update them and and make new yeah
    um update them and and make new

    ones. So yeah, they should work pretty ones. So yeah, they should work pretty
    ones. So yeah, they should work pretty

    well for it. >> Cool. But yeah, but I think in general >> Cool. But yeah, but
    I think in general

    you can also build your own um if you you can also build your own um if you you
    can also build your own um if you

    don''t like my style of doing things don''t like my style of doing things don''t
    like my style of doing things

    honestly. And it''s like I''m like pretty honestly. And it''s like I''m like pretty
    honestly. And it''s like I''m like pretty

    sure Claw can just do it for you and you sure Claw can just do it for you and
    you sure Claw can just do it for you and you

    just need to do minor debugging and just need to do minor debugging and just need
    to do minor debugging and

    that''s fine. Yeah. that''s fine. Yeah. that''s fine. Yeah.

    >> Okay. Any other questions? Okay. Seems like we''re all good, Okay. Seems like
    we''re all good,

    Charles. Thank you so much. Charles. Thank you so much. Charles. Thank you so
    much.

    >> All right. Yeah. Thanks a lot, Kelly. >> All right. Yeah. Thanks a lot, Kelly.
    >> All right. Yeah. Thanks a lot, Kelly.

    All right. Take care, everyone. Bye. All right. Take care, everyone. Bye. All
    right. Take care, everyone. Bye.

    Bye. Bye. Bye.

    >> Yeah. Thank you. Bye. Bye.'
  concept_slugs: []
---
# CMU 10799 S26: Lecture 3 - Modal Guest Lecture - Diffusion & Flow Matching

See the structured chunks above.
