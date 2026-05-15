---
course_slug: cmu-10799-diffusion-flow
idx: 3
title: 'CMU 10799 S26: Lecture 2 - Denoising Diffusion Models - Diffusion & Flow Matching'
video_url: https://www.youtube.com/watch?v=H-RbhdiWzto
duration_sec: null
chunks:
- idx: 0
  start_sec: 3.27
  end_sec: 49.76
  text: 'Cool. Hello everyone. Oh, it''s not Cool. Hello everyone. Oh, it''s not

    significantly fewer. I guess it''s significantly fewer. I guess it''s significantly
    fewer. I guess it''s

    slightly significant. Okay, cool slightly significant. Okay, cool slightly significant.
    Okay, cool

    everyone. Hello. Welcome to lecture two. everyone. Hello. Welcome to lecture two.
    everyone. Hello. Welcome to lecture two.

    Uh today we''re going to be talking about Uh today we''re going to be talking
    about Uh today we''re going to be talking about

    diffusion models finally. Uh yeah, we diffusion models finally. Uh yeah, we diffusion
    models finally. Uh yeah, we

    spent the last uh last uh lecture not spent the last uh last uh lecture not spent
    the last uh last uh lecture not

    talking about diffusion model in the talking about diffusion model in the talking
    about diffusion model in the

    diffusion class, but I guess this time diffusion class, but I guess this time
    diffusion class, but I guess this time

    we finally gonna talk about diffusion we finally gonna talk about diffusion we
    finally gonna talk about diffusion

    model now. All right. So before we model now. All right. So before we model now.
    All right. So before we

    actually get actually get actually get

    started, a couple of like housekeeping started, a couple of like housekeeping
    started, a couple of like housekeeping

    items that we want to take care of. Uh items that we want to take care of. Uh
    items that we want to take care of. Uh

    so the first thing is the homework is so the first thing is the homework is so
    the first thing is the homework is

    out now and it''s actually due fairly out now and it''s actually due fairly out
    now and it''s actually due fairly

    soon. It''s due in like 10 days uh or soon. It''s due in like 10 days uh or soon.
    It''s due in like 10 days uh or

    nine days I guess. So like just try to nine days I guess. So like just try to
    nine days I guess. So like just try to

    start early because training model start early because training model start early
    because training model

    actually takes time. So I I I I mean it actually takes time. So I I I I mean it'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 1
  start_sec: 49.76
  end_sec: 81.6
  text: 'actually takes time. So I I I I mean it

    it takes at least a couple of hours uh it takes at least a couple of hours uh
    it takes at least a couple of hours uh

    on GPU. on GPU. on GPU.

    Do not even try to train models on CPU. Do not even try to train models on CPU.
    Do not even try to train models on CPU.

    It''s just not going to it''s not going to It''s just not going to it''s not going
    to It''s just not going to it''s not going to

    not going to work. Well, I mean it''s not going to work. Well, I mean it''s not
    going to work. Well, I mean it''s

    going to work, but it''s just like it''s going to work, but it''s just like it''s
    going to work, but it''s just like it''s

    going to take you like 100 years. Do not going to take you like 100 years. Do
    not going to take you like 100 years. Do not

    do that. Um but yeah, you will be do that. Um but yeah, you will be do that. Um
    but yeah, you will be

    getting uh well, I guess I talk about it getting uh well, I guess I talk about
    it getting uh well, I guess I talk about it

    later, but yeah, just try to start it later, but yeah, just try to start it later,
    but yeah, just try to start it

    early. At least take a look at it. Even early. At least take a look at it. Even
    early. At least take a look at it. Even

    if you do not have GPU right now, you if you do not have GPU right now, you if
    you do not have GPU right now, you

    can still start to do things now can still start to do things now can still start
    to do things now

    actually if you take a look at the actually if you take a look at the actually
    if you take a look at the

    homework. Um, and uh, yeah, so our homework. Um, and uh, yeah, so our homework.
    Um, and uh, yeah, so our

    sponsor is going to give us a guest sponsor is going to give us a guest'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 2
  start_sec: 81.6
  end_sec: 118.96
  text: 'sponsor is going to give us a guest

    lecture tomorrow. So, if you are going lecture tomorrow. So, if you are going
    lecture tomorrow. So, if you are going

    to be using the sponsor credit, I think to be using the sponsor credit, I think
    to be using the sponsor credit, I think

    it''s like a very good idea to just uh, it''s like a very good idea to just uh,
    it''s like a very good idea to just uh,

    check it out because they''re going to be check it out because they''re going
    to be check it out because they''re going to be

    basically um, giving a tutorial on how basically um, giving a tutorial on how
    basically um, giving a tutorial on how

    to use their service and it''s actually to use their service and it''s actually
    to use their service and it''s actually

    really really simple. I feel like with really really simple. I feel like with
    really really simple. I feel like with

    the clock code or like cursor, you can the clock code or like cursor, you can
    the clock code or like cursor, you can

    just literally do it. Yeah. just literally do it. Yeah. just literally do it.
    Yeah.

    >> Yes, it''s going to be recorded. So, yes, >> Yes, it''s going to be recorded.
    So, yes, >> Yes, it''s going to be recorded. So, yes,

    that''s right. Uh I in the homework I that''s right. Uh I in the homework I that''s
    right. Uh I in the homework I

    actually also already provide you guys actually also already provide you guys
    actually also already provide you guys

    with like supposed to be working uh you with like supposed to be working uh you
    with like supposed to be working uh you

    know just um like model integration. So know just um like model integration. So
    know just um like model integration. So

    hopefully it''s just going to work. Uh hopefully it''s just going to work. Uh
    hopefully it''s just going to work. Uh

    but if it doesn''t just like just debug but if it doesn''t just like just debug
    but if it doesn''t just like just debug

    with cloud and it''s it''s going to work with cloud and it''s it''s going to work'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 3
  start_sec: 118.96
  end_sec: 161.11
  text: 'with cloud and it''s it''s going to work

    I''m sure. Um and I already tested so so I''m sure. Um and I already tested so
    so I''m sure. Um and I already tested so so

    it should work. And uh the Oh yes, and it should work. And uh the Oh yes, and
    it should work. And uh the Oh yes, and

    about Friday uh because the last day to about Friday uh because the last day to
    about Friday uh because the last day to

    add class to add class to add class to

    minis 3 is going to be Friday. So we''re minis 3 is going to be Friday. So we''re
    minis 3 is going to be Friday. So we''re

    going to just be like moving along on of going to just be like moving along on
    of going to just be like moving along on of

    the wait list until Friday. Um yeah. So the wait list until Friday. Um yeah. So
    the wait list until Friday. Um yeah. So

    so basically just if you so basically just if you so basically just if you

    want still want a chance to get added to want still want a chance to get added
    to want still want a chance to get added to

    the class, just stay on the wait list the class, just stay on the wait list the
    class, just stay on the wait list

    for like another day and then you you''re for like another day and then you you''re
    for like another day and then you you''re

    going to know. Um, so like a lot of going to know. Um, so like a lot of going
    to know. Um, so like a lot of

    people message me about like basically, people message me about like basically,
    people message me about like basically,

    oh, I I don''t know if I''m gonna get into oh, I I don''t know if I''m gonna get
    into oh, I I don''t know if I''m gonna get into

    the class. Uh, so yeah. So basically the the class. Uh, so yeah. So basically
    the the class. Uh, so yeah. So basically the

    the ad deadline is a little bit earlier the ad deadline is a little bit earlier
    the ad deadline is a little bit earlier

    for the mini class than the semester'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 4
  start_sec: 161.11
  end_sec: 203.36
  text: 'for the mini class than the semester for the mini class than the semester

    class. So I think you guys are going to class. So I think you guys are going to
    class. So I think you guys are going to

    be more or less okay to decide whether be more or less okay to decide whether
    be more or less okay to decide whether

    or not you want to just like do the or not you want to just like do the or not
    you want to just like do the

    backup option backup option backup option

    after tomorrow, I think. Um and uh yeah after tomorrow, I think. Um and uh yeah
    after tomorrow, I think. Um and uh yeah

    because we are going to be uh you know because we are going to be uh you know
    because we are going to be uh you know

    still adding people. So we are going to still adding people. So we are going to
    still adding people. So we are going to

    uh like nobody has been added to the uh like nobody has been added to the uh like
    nobody has been added to the

    register student channel on discord yet register student channel on discord yet
    register student channel on discord yet

    and once we have finalized the list and once we have finalized the list and once
    we have finalized the list

    we''re going to add everyone to the we''re going to add everyone to the we''re
    going to add everyone to the

    channel and then we''re going to send out channel and then we''re going to send
    out channel and then we''re going to send out

    the coupon in that channel. So make sure the coupon in that channel. So make sure
    the coupon in that channel. So make sure

    to check out the discord messages to check out the discord messages to check out
    the discord messages

    tomorrow. tomorrow. tomorrow.

    Um but yeah and another thing is that if Um but yeah and another thing is that
    if Um but yeah and another thing is that if

    you''re auditing you do not need to do you''re auditing you do not need to do
    you''re auditing you do not need to do

    anything. Okay, you don''t you do not anything. Okay, you don''t you do not'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 5
  start_sec: 203.36
  end_sec: 244.159
  text: 'anything. Okay, you don''t you do not

    need to submit any forms. Like it''s just need to submit any forms. Like it''s
    just need to submit any forms. Like it''s just

    like basically the the the the thing is like basically the the the the thing is
    like basically the the the the thing is

    that like in order to officially audit, that like in order to officially audit,
    that like in order to officially audit,

    you''ll need to be a I need to be able to you''ll need to be a I need to be able
    to you''ll need to be a I need to be able to

    give you a grade somehow about your give you a grade somehow about your give you
    a grade somehow about your

    participation, but there''s like no participation, but there''s like no participation,
    but there''s like no

    participation grade in this class. So, participation grade in this class. So,
    participation grade in this class. So,

    it doesn''t make sense. Um and the it doesn''t make sense. Um and the it doesn''t
    make sense. Um and the

    only difference between the auditing only difference between the auditing only
    difference between the auditing

    student and the officially registered student and the officially registered student
    and the officially registered

    student is that a you do not get credit. student is that a you do not get credit.
    student is that a you do not get credit.

    Sorry, you do not get class credit. So, Sorry, you do not get class credit. So,
    Sorry, you do not get class credit. So,

    you cannot just like use this class for you cannot just like use this class for
    you cannot just like use this class for

    your degree if you want to if you''re your degree if you want to if you''re your
    degree if you want to if you''re

    auditing. Uh the second thing is that auditing. Uh the second thing is that auditing.
    Uh the second thing is that

    you are not going to get GPU credits you are not going to get GPU credits you
    are not going to get GPU credits

    from the sponsor. And third thing, from the sponsor. And third thing, from the
    sponsor. And third thing,

    obviously I cannot grade you. Uh but if obviously I cannot grade you. Uh but if'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 6
  start_sec: 244.159
  end_sec: 278.96
  text: 'obviously I cannot grade you. Uh but if

    you want to say like sit in a class you want to say like sit in a class you want
    to say like sit in a class

    which are you already did um and or uh which are you already did um and or uh
    which are you already did um and or uh

    you know come to office hours or even if you know come to office hours or even
    if you know come to office hours or even if

    you want to like uh you know present you want to like uh you know present you
    want to like uh you know present

    your work at the poster session, we can your work at the poster session, we can
    your work at the poster session, we can

    make that happen for sure. So like just make that happen for sure. So like just
    make that happen for sure. So like just

    the everything else is fine. It''s just the everything else is fine. It''s just
    the everything else is fine. It''s just

    that I cannot give you money or credit that I cannot give you money or credit
    that I cannot give you money or credit

    basically. Um and uh the last thing is basically. Um and uh the last thing is
    basically. Um and uh the last thing is

    that we''re going to have our first quiz that we''re going to have our first quiz
    that we''re going to have our first quiz

    uh next class. I was going to do it this uh next class. I was going to do it this
    uh next class. I was going to do it this

    class but then I realized that you know class but then I realized that you know
    class but then I realized that you know

    not everyone has been registered so it''s not everyone has been registered so
    it''s not everyone has been registered so it''s

    not doesn''t make sense to do it this not doesn''t make sense to do it this not
    doesn''t make sense to do it this

    class but yeah we''re going to do our class but yeah we''re going to do our class
    but yeah we''re going to do our

    first quiz next next class is just going first quiz next next class is just going'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 7
  start_sec: 278.96
  end_sec: 317.919
  text: 'first quiz next next class is just going

    to be the things that we have learned to be the things that we have learned to
    be the things that we have learned

    throughout this week. There will be no throughout this week. There will be no
    throughout this week. There will be no

    math. Don''t worry, I will not like I math. Don''t worry, I will not like I math.
    Don''t worry, I will not like I

    will not let you derive things on the will not let you derive things on the will
    not let you derive things on the

    spot in 10 minutes. That doesn''t make spot in 10 minutes. That doesn''t make
    spot in 10 minutes. That doesn''t make

    sense. And you have Chad GPT now. You sense. And you have Chad GPT now. You sense.
    And you have Chad GPT now. You

    don''t need to do that. But yeah, it''s don''t need to do that. But yeah, it''s
    don''t need to do that. But yeah, it''s

    just going to be like concept check just going to be like concept check just going
    to be like concept check

    basically. So do not worry too much. If basically. So do not worry too much. If
    basically. So do not worry too much. If

    you have pay attention to class, you you have pay attention to class, you you
    have pay attention to class, you

    should be able to answer them. All should be able to answer them. All should be
    able to answer them. All

    right, cool. So basically last class we right, cool. So basically last class we
    right, cool. So basically last class we

    have talked about what is probabilistic have talked about what is probabilistic
    have talked about what is probabilistic

    modeling which hopefully you guys modeling which hopefully you guys modeling which
    hopefully you guys

    already know what it is and we also already know what it is and we also already
    know what it is and we also

    talked about genetic modeling which is talked about genetic modeling which is
    talked about genetic modeling which is

    bas bas bas

    basically we''re trying to model the basically we''re trying to model the basically
    we''re trying to model the

    distribution of the data so that we can distribution of the data so that we can'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 8
  start_sec: 317.919
  end_sec: 366.72
  text: 'distribution of the data so that we can

    actually draw new samples from it. Yeah. actually draw new samples from it. Yeah.
    actually draw new samples from it. Yeah.

    And we have looked at a couple of And we have looked at a couple of And we have
    looked at a couple of

    genetic models for example auto genetic models for example auto genetic models
    for example auto

    reggressive modeling which is a LM and reggressive modeling which is a LM and
    reggressive modeling which is a LM and

    then we have also looked at GANs which then we have also looked at GANs which
    then we have also looked at GANs which

    is like you know this like zero sum game is like you know this like zero sum game
    is like you know this like zero sum game

    that that the generator and the that that the generator and the that that the
    generator and the

    discriminator discriminator discriminator

    is playing and very importantly uh we is playing and very importantly uh we is
    playing and very importantly uh we

    also looked at VAE right so uh right now also looked at VAE right so uh right
    now also looked at VAE right so uh right now

    we''re going to give a recap and also a we''re going to give a recap and also
    a we''re going to give a recap and also a

    deeper look into what exactly is VAE How deeper look into what exactly is VAE
    How deeper look into what exactly is VAE How

    do we train one? And everything that we do we train one? And everything that we
    do we train one? And everything that we

    learn in VAE is going to be like super learn in VAE is going to be like super
    learn in VAE is going to be like super

    super relevant when we try to develop super relevant when we try to develop super
    relevant when we try to develop

    diffusion models. Okay. So what is VAE? diffusion models. Okay. So what is VAE?
    diffusion models. Okay. So what is VAE?

    Given a uh data sample, you basically Given a uh data sample, you basically Given
    a uh data sample, you basically

    you try you try to learn an encoder so you try you try to learn an encoder so'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 9
  start_sec: 366.72
  end_sec: 407.99
  text: 'you try you try to learn an encoder so

    that it can encode it into some latent that it can encode it into some latent
    that it can encode it into some latent

    space. Uh and then like it is an space. Uh and then like it is an space. Uh and
    then like it is an

    autoenccoder. So it''s also trying to autoenccoder. So it''s also trying to autoenccoder.
    So it''s also trying to

    decode it back to the data space so that decode it back to the data space so that
    decode it back to the data space so that

    you have this like sort of like a like you have this like sort of like a like
    you have this like sort of like a like

    like a tunnel uh uh reconstruction going like a tunnel uh uh reconstruction going
    like a tunnel uh uh reconstruction going

    on. Um so in order to be able to model on. Um so in order to be able to model
    on. Um so in order to be able to model

    this hidden variable we need to do two this hidden variable we need to do two
    this hidden variable we need to do two

    things. Uh so we need to a maximize the things. Uh so we need to a maximize the
    things. Uh so we need to a maximize the

    likelihood of the data. Uh so this is likelihood of the data. Uh so this is likelihood
    of the data. Uh so this is

    like basically just all likelihood based like basically just all likelihood based
    like basically just all likelihood based

    the general model what they''re doing and the general model what they''re doing
    and the general model what they''re doing and

    second thing is we need to make sure second thing is we need to make sure second
    thing is we need to make sure

    that this is like a valid uh like that this is like a valid uh like that this
    is like a valid uh like

    autoenccoder right? So basically what autoenccoder right? So basically what autoenccoder
    right? So basically what

    what we what we''re trying to do is we''re what we what we''re trying to do is
    we''re what we what we''re trying to do is we''re

    trying to make sure that this encoding'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 10
  start_sec: 407.99
  end_sec: 453.67
  text: 'trying to make sure that this encoding trying to make sure that this encoding

    this notion of of encoding is the same this notion of of encoding is the same
    this notion of of encoding is the same

    for both encoder and decoder. What it for both encoder and decoder. What it for
    both encoder and decoder. What it

    means is that the the encoder needs to means is that the the encoder needs to
    means is that the the encoder needs to

    basically the the the distribution of Z basically the the the distribution of
    Z basically the the the distribution of Z

    that the encoder induced need to be the that the encoder induced need to be the
    that the encoder induced need to be the

    same same same

    that the one that decoder is going to that the one that decoder is going to that
    the one that decoder is going to

    use to generate data samples. Okay. So use to generate data samples. Okay. So
    use to generate data samples. Okay. So

    yeah. So basically here''s what we what yeah. So basically here''s what we what
    yeah. So basically here''s what we what

    we can design in a VAE is that we can we can design in a VAE is that we can we
    can design in a VAE is that we can

    design the prior distribution of the Z design the prior distribution of the Z
    design the prior distribution of the Z

    that we can sample from and we can also that we can sample from and we can also
    that we can sample from and we can also

    design the encoder essentially um and we design the encoder essentially um and
    we design the encoder essentially um and we

    can also design the decoder. So the can also design the decoder. So the can also
    design the decoder. So the

    encoder meaning that we encode from a encoder meaning that we encode from a encoder
    meaning that we encode from a

    data to a latent and then decoder means data to a latent and then decoder means
    data to a latent and then decoder means

    that we like decode from a latent to that we like decode from a latent to that
    we like decode from a latent to

    data. Okay. So this is what we can'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 11
  start_sec: 453.67
  end_sec: 501.189
  text: 'data. Okay. So this is what we can data. Okay. So this is what we can

    design but what we do not have is uh design but what we do not have is uh design
    but what we do not have is uh

    basically the the actual likelihood of basically the the actual likelihood of
    basically the the actual likelihood of

    the data that we want and also the the data that we want and also the the data
    that we want and also the

    basically what kind of Z what what kind basically what kind of Z what what kind
    basically what kind of Z what what kind

    of latent can produce your data and this of latent can produce your data and this
    of latent can produce your data and this

    is basically just saying that we do not is basically just saying that we do not
    is basically just saying that we do not

    know what kind of genes know what kind of genes know what kind of genes

    is going to produce a human like it is I is going to produce a human like it is
    I is going to produce a human like it is I

    mean we we could know but it''s not like mean we we could know but it''s not like
    mean we we could know but it''s not like

    it''s it''s not observable immediately it''s it''s not observable immediately
    it''s it''s not observable immediately

    right um but what we want uh is these right um but what we want uh is these right
    um but what we want uh is these

    three things based on our uh based on three things based on our uh based on three
    things based on our uh based on

    the objective that we derived. Right? So the objective that we derived. Right?
    So the objective that we derived. Right? So

    basically um so what we''re trying to do basically um so what we''re trying to
    do basically um so what we''re trying to do

    is we''re trying to maximize the is we''re trying to maximize the is we''re trying
    to maximize the

    likelihood of the data and then we also likelihood of the data and then we also
    likelihood of the data and then we also

    try to make sure that um the encoder and'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 12
  start_sec: 501.189
  end_sec: 549.2
  text: 'try to make sure that um the encoder and try to make sure that um the encoder
    and

    decoder are induced by the same um like decoder are induced by the same um like
    decoder are induced by the same um like

    distribution of Z given X. Um so yeah so distribution of Z given X. Um so yeah
    so distribution of Z given X. Um so yeah so

    then we did deduce the the elbow then we did deduce the the elbow then we did
    deduce the the elbow

    which is basically uh composed of the which is basically uh composed of the which
    is basically uh composed of the

    reconstruction loss from the encoded reconstruction loss from the encoded reconstruction
    loss from the encoded

    decoder and also a kale regularization decoder and also a kale regularization
    decoder and also a kale regularization

    right and then we we looked at two ways right and then we we looked at two ways
    right and then we we looked at two ways

    to derive the elbow uh let''s take a to derive the elbow uh let''s take a to derive
    the elbow uh let''s take a

    deeper look at the second way so deeper look at the second way so deeper look
    at the second way so

    basically how you do it is you start basically how you do it is you start basically
    how you do it is you start

    from your likelihood your your your data from your likelihood your your your data
    from your likelihood your your your data

    likelihood and then you basically just likelihood and then you basically just
    likelihood and then you basically just

    decompose the p of x part into a decompose the p of x part into a decompose the
    p of x part into a

    integral of the joint distribution integral of the joint distribution integral
    of the joint distribution

    between the data and the and the latent between the data and the and the latent
    between the data and the and the latent

    and then you do the greatest and then you do the greatest and then you do the
    greatest

    mathematical trick of the of all time. mathematical trick of the of all time.
    mathematical trick of the of all time.

    You multiply by something and divide it You multiply by something and divide it'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 13
  start_sec: 549.2
  end_sec: 600.959
  text: 'You multiply by something and divide it

    by something and then you get a equal by something and then you get a equal by
    something and then you get a equal

    sign, right? Uh and basically this thing sign, right? Uh and basically this thing
    sign, right? Uh and basically this thing

    will give you a uh a expectation because will give you a uh a expectation because
    will give you a uh a expectation because

    this is integral of some probability this is integral of some probability this
    is integral of some probability

    distribution uh of and yeah you distribution uh of and yeah you distribution uh
    of and yeah you

    integrate over those things right. integrate over those things right. integrate
    over those things right.

    That''s the definition of uh expectation. That''s the definition of uh expectation.
    That''s the definition of uh expectation.

    And And And

    here we channel a very very very here we channel a very very very here we channel
    a very very very

    important inequality. It''s what we call important inequality. It''s what we call
    important inequality. It''s what we call

    a Jensen''s inequality. Uh so not this a Jensen''s inequality. Uh so not this
    a Jensen''s inequality. Uh so not this

    guy, right? Not the guy that that that guy, right? Not the guy that that that
    guy, right? Not the guy that that that

    that gives you GPU. It''s the it''s this that gives you GPU. It''s the it''s this
    that gives you GPU. It''s the it''s this

    guy. It''s a mathematician. Uh so guy. It''s a mathematician. Uh so guy. It''s
    a mathematician. Uh so

    basically what this Jensen inequality is basically what this Jensen inequality
    is basically what this Jensen inequality is

    is that if your function is convex then is that if your function is convex then
    is that if your function is convex then

    the expectation of the function is the expectation of the function is the expectation
    of the function is

    greater than or equal to the function greater than or equal to the function greater
    than or equal to the function

    applied to the expectation and similarly applied to the expectation and similarly
    applied to the expectation and similarly

    if your function is con concave then the if your function is con concave then
    the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 14
  start_sec: 600.959
  end_sec: 656.8
  text: 'if your function is con concave then the

    the sign flips. So here the log function the sign flips. So here the log function
    the sign flips. So here the log function

    is a concave function. So that''s why we is a concave function. So that''s why
    we is a concave function. So that''s why we

    can have this inequality here. Okay. So can have this inequality here. Okay. So
    can have this inequality here. Okay. So

    now that you can bring the log inside now that you can bring the log inside now
    that you can bring the log inside

    this just like decompose you just this just like decompose you just this just
    like decompose you just

    decompose everything and then it''s going decompose everything and then it''s
    going decompose everything and then it''s going

    to give you the exact elbow that we''re to give you the exact elbow that we''re
    to give you the exact elbow that we''re

    having. Okay, so far so good. Is there having. Okay, so far so good. Is there
    having. Okay, so far so good. Is there

    any questions here? any questions here? any questions here?

    All right, good. All right, good. All right, good.

    Cool. All right, so now that we have an Cool. All right, so now that we have an
    Cool. All right, so now that we have an

    elbow, how exactly elbow, how exactly elbow, how exactly

    should we train a VAE? Right. Basically, should we train a VAE? Right. Basically,
    should we train a VAE? Right. Basically,

    if you if you take a good look at it if you if you take a good look at it if you
    if you take a good look at it

    this elbow, you''ll notice that this elbow, you''ll notice that this elbow, you''ll
    notice that

    basically both part of the elbow will basically both part of the elbow will basically
    both part of the elbow will

    require us to sample from this require us to sample from this require us to sample
    from this

    distribution of qz given x. Um so that distribution of qz given x. Um so that
    distribution of qz given x. Um so that

    just means that this like just means that this like just means that this like

    remember like this thing like we do not remember like this thing like we do not'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 15
  start_sec: 656.8
  end_sec: 696.399
  text: 'remember like this thing like we do not

    have a sampler of x, right? So we just have a sampler of x, right? So we just
    have a sampler of x, right? So we just

    we need a sampler over z that is like we need a sampler over z that is like we
    need a sampler over z that is like

    that we can differentiate through. So that we can differentiate through. So that
    we can differentiate through. So

    this is a sampler. This is not like you this is a sampler. This is not like you
    this is a sampler. This is not like you

    you do not have data sample at a test you do not have data sample at a test you
    do not have data sample at a test

    time anymore. Right? So basically we time anymore. Right? So basically we time
    anymore. Right? So basically we

    need a sampler that we can differentiate need a sampler that we can differentiate
    need a sampler that we can differentiate

    through so that we can learn it. This is through so that we can learn it. This
    is through so that we can learn it. This is

    the first thing and then the second the first thing and then the second the first
    thing and then the second

    thing is that because we can choose this thing is that because we can choose this
    thing is that because we can choose this

    is just like a standalone prior right. is just like a standalone prior right.
    is just like a standalone prior right.

    So we can just like choose whichever So we can just like choose whichever So we
    can just like choose whichever

    prior that we want. So it should be prior that we want. So it should be prior
    that we want. So it should be

    something that is like really really something that is like really really something
    that is like really really

    simple or has a very simple log form. simple or has a very simple log form. simple
    or has a very simple log form.

    Okay. So given these information, can Okay. So given these information, can Okay.
    So given these information, can

    anyone take a guess of like what what anyone take a guess of like what what'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 16
  start_sec: 696.399
  end_sec: 748.47
  text: 'anyone take a guess of like what what

    kind of parameterization that we''re kind of parameterization that we''re kind
    of parameterization that we''re

    going to use here? going to use here? going to use here?

    >> Yes. Why who who said gausian? Why do >> Yes. Why who who said gausian? Why
    do >> Yes. Why who who said gausian? Why do

    you say gausian? you say gausian? you say gausian?

    Oh, I mean I mean why do you think Oh, I mean I mean why do you think Oh, I mean
    I mean why do you think

    gausian is a good idea? Sorry. Yeah. gausian is a good idea? Sorry. Yeah. gausian
    is a good idea? Sorry. Yeah.

    >> Very simple simple distribution and >> Very simple simple distribution and
    >> Very simple simple distribution and

    works. works. works.

    >> Very nice. This is exactly the answer. >> Very nice. This is exactly the answer.
    >> Very nice. This is exactly the answer.

    Uh so this thing is what we need. uh Uh so this thing is what we need. uh Uh so
    this thing is what we need. uh

    what we learned as the what we learned as the what we learned as the

    reparameterization trick. All right. So reparameterization trick. All right. So
    reparameterization trick. All right. So

    like what''s your name? like what''s your name? like what''s your name?

    >> R >> R >> R

    >> roof. >> roof. >> roof.

    >> Okay. R said this is let''s just choose >> Okay. R said this is let''s just
    choose >> Okay. R said this is let''s just choose

    the simplest distribution here. All the simplest distribution here. All the simplest
    distribution here. All

    right. Uh the standard normal gausian uh right. Uh the standard normal gausian
    uh right. Uh the standard normal gausian uh

    as the as the prior because we can as the as the prior because we can as the as
    the prior because we can

    choose anything. So let''s just choose choose anything. So let''s just choose
    choose anything. So let''s just choose

    the simplest one. All right. Uh then the simplest one. All right. Uh then the
    simplest one. All right. Uh then

    what would be the easiest way to what would be the easiest way to what would be
    the easiest way to

    parameterize Q Z uh Z over uh Z given'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 17
  start_sec: 748.47
  end_sec: 795.519
  text: 'parameterize Q Z uh Z over uh Z given parameterize Q Z uh Z over uh Z given

    accent also a gausian also gausian right uh so also a gausian also gausian right
    uh so

    basically it just just you just choose a basically it just just you just choose
    a basically it just just you just choose a

    bunch of gausian right uh so remember bunch of gausian right uh so remember bunch
    of gausian right uh so remember

    how you should tattoo uh like bay rule how you should tattoo uh like bay rule
    how you should tattoo uh like bay rule

    on your wrist the other you have two on your wrist the other you have two on your
    wrist the other you have two

    wrists the other wrist you should tattoo wrists the other wrist you should tattoo
    wrists the other wrist you should tattoo

    the face of gausian basically this guy the face of gausian basically this guy
    the face of gausian basically this guy

    is like so goatated that like the the is like so goatated that like the the is
    like so goatated that like the the

    the the distribution that he developed the the distribution that he developed
    the the distribution that he developed

    is just like the the standard the normal is just like the the standard the normal
    is just like the the standard the normal

    now it''s just like you imagine the thing now it''s just like you imagine the
    thing now it''s just like you imagine the thing

    that you invented is it just it just the that you invented is it just it just
    the that you invented is it just it just the

    normal thing it''s crazy all right anyway normal thing it''s crazy all right anyway
    normal thing it''s crazy all right anyway

    it''s very goated let''s remember him and it''s very goated let''s remember him
    and it''s very goated let''s remember him and

    uh so basically let''s just if we choose uh so basically let''s just if we choose
    uh so basically let''s just if we choose

    q of z given x like the parameterization q of z given x like the parameterization
    q of z given x like the parameterization

    of it to be a diagonal gausian then we of it to be a diagonal gausian then we'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 18
  start_sec: 795.519
  end_sec: 845.12
  text: 'of it to be a diagonal gausian then we

    can literally just write out the par the can literally just write out the par
    the can literally just write out the par the

    parameters of the distribution like this parameters of the distribution like this
    parameters of the distribution like this

    right so basically All you need to learn right so basically All you need to learn
    right so basically All you need to learn

    are two things the mean and the standard are two things the mean and the standard
    are two things the mean and the standard

    deviation right or the mean and the deviation right or the mean and the deviation
    right or the mean and the

    variance. Uh then basically uh so to variance. Uh then basically uh so to variance.
    Uh then basically uh so to

    sample from this distribution all you sample from this distribution all you sample
    from this distribution all you

    need to do is you need to first sample need to do is you need to first sample
    need to do is you need to first sample

    from a standard normal which is we know from a standard normal which is we know
    from a standard normal which is we know

    how to do uh and then you just scale it how to do uh and then you just scale it
    how to do uh and then you just scale it

    right you just like shift and scale right you just like shift and scale right
    you just like shift and scale

    using your learn the mean and standard using your learn the mean and standard
    using your learn the mean and standard

    deviation. Uh so so that that''s deviation. Uh so so that that''s deviation. Uh
    so so that that''s

    basically that. All right. So now we basically that. All right. So now we basically
    that. All right. So now we

    have a very very nice form of Q Z and P have a very very nice form of Q Z and
    P have a very very nice form of Q Z and P

    theta Z. All right. Uh theta Z. All right. Uh theta Z. All right. Uh

    okay. Okay. So because we have this and okay. Okay. So because we have this and'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 19
  start_sec: 845.12
  end_sec: 888.959
  text: 'okay. Okay. So because we have this and

    both of them are Gaussian. Uh so that both of them are Gaussian. Uh so that both
    of them are Gaussian. Uh so that

    this KL actually has a closed form. So this KL actually has a closed form. So
    this KL actually has a closed form. So

    basically how you deduce this is you basically how you deduce this is you basically
    how you deduce this is you

    literally just write out the log literally just write out the log literally just
    write out the log

    likelihood of Gausian distribution and likelihood of Gausian distribution and
    likelihood of Gausian distribution and

    then you would arrive at this basically. then you would arrive at this basically.
    then you would arrive at this basically.

    So but I''m just going to give you the So but I''m just going to give you the
    So but I''m just going to give you the

    the formula here. This is this is the the formula here. This is this is the the
    formula here. This is this is the

    closed form solution to the second part closed form solution to the second part
    closed form solution to the second part

    of the elbow. Okay. All right. Now what of the elbow. Okay. All right. Now what
    of the elbow. Okay. All right. Now what

    about the first part then like we solved about the first part then like we solved
    about the first part then like we solved

    the second part. The first part we kind the second part. The first part we kind
    the second part. The first part we kind

    of solved the like like the half of the of solved the like like the half of the
    of solved the like like the half of the

    first part as well. Then what about the first part as well. Then what about the
    first part as well. Then what about the

    log p theta x given z uh which is the log p theta x given z uh which is the log
    p theta x given z uh which is the

    reconstructor or the decoder. How should reconstructor or the decoder. How should
    reconstructor or the decoder. How should

    we how should we parameterize the we how should we parameterize the we how should
    we parameterize the

    decoder? decoder?'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 20
  start_sec: 888.959
  end_sec: 958.399
  text: 'decoder?

    Anyone want to take a guess? Maybe a gian mixture more because like Maybe a gian
    mixture more because like

    gosh is more. >> Yeah. Yeah. Yeah. Yeah. Yeah. Yeah. >> Yeah. Yeah. Yeah. Yeah.
    Yeah. Yeah.

    Yeah. Yeah. Yes. Basically, we just we Yeah. Yeah. Yes. Basically, we just we
    Yeah. Yeah. Yes. Basically, we just we

    just need something that you can just need something that you can just need something
    that you can

    calculate the log likelihood easily. So, calculate the log likelihood easily.
    So, calculate the log likelihood easily. So,

    it just this golden man basically just it just this golden man basically just
    it just this golden man basically just

    is also gausian. Um why do you basically is also gausian. Um why do you basically
    is also gausian. Um why do you basically

    why don''t you need multi-modality here? why don''t you need multi-modality here?
    why don''t you need multi-modality here?

    Well, it''s because this is like a learn Well, it''s because this is like a learn
    Well, it''s because this is like a learn

    the very highdimensional thing. So like the very highdimensional thing. So like
    the very highdimensional thing. So like

    basically you you like you are learning basically you you like you are learning
    basically you you like you are learning

    the basically you can you can sort of the basically you can you can sort of the
    basically you can you can sort of

    actually this actually this actually this

    like va is not optimal basically but but like va is not optimal basically but
    but like va is not optimal basically but but

    but like you could just assume that this but like you could just assume that this
    but like you could just assume that this

    is also a gausian with some small is also a gausian with some small is also a
    gausian with some small

    variance then all you need to do is to variance then all you need to do is to
    variance then all you need to do is to

    learn the mean essentially. Yeah. then learn the mean essentially. Yeah. then
    learn the mean essentially. Yeah. then

    the reconstruction laws will become also the reconstruction laws will become also
    the reconstruction laws will become also

    closed form closed form closed form

    and then uh and then uh'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 21
  start_sec: 958.399
  end_sec: 1024.559
  text: 'and then uh

    it''s uh magically it''s uh magically it''s uh magically

    something that that is basically L2. So something that that is basically L2. So
    something that that is basically L2. So

    that''s why it''s called reconstruction that''s why it''s called reconstruction
    that''s why it''s called reconstruction

    loss because it''s literally like how loss because it''s literally like how loss
    because it''s literally like how

    good you how good your p like predicted good you how good your p like predicted
    good you how good your p like predicted

    value from your decoder can reproduce value from your decoder can reproduce value
    from your decoder can reproduce

    the the data sample because it''s the the data sample because it''s the the data
    sample because it''s

    literally L2. literally L2. literally L2.

    Okay. Or MSE. Yeah. Um, why is it that like Um, why is it that like

    does it imply that like x can go into does it imply that like x can go into does
    it imply that like x can go into

    like a whole distribution? like a whole distribution? like a whole distribution?

    >> Wouldn''t you want to do it because >> Wouldn''t you want to do it because
    >> Wouldn''t you want to do it because

    >> uh why would you want to do that? >> uh why would you want to do that? >> uh
    why would you want to do that?

    Because okay, let''s give you let me give Because okay, let''s give you let me
    give Because okay, let''s give you let me give

    you like analogy. It''s but it actually you like analogy. It''s but it actually
    you like analogy. It''s but it actually

    cause some problem later than we''re cause some problem later than we''re cause
    some problem later than we''re

    going to talk about. So basically going to talk about. So basically going to talk
    about. So basically

    imagine that like you you human has imagine that like you you human has imagine
    that like you you human has

    genes, right? the human genes is genes, right? the human genes is genes, right?
    the human genes is

    actually like not every part of the actually like not every part of the actually
    like not every part of the

    genes is like expressive. So basically genes is like expressive. So basically'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 22
  start_sec: 1024.559
  end_sec: 1073.669
  text: 'genes is like expressive. So basically

    they have some like lazy genes. This is they have some like lazy genes. This is
    they have some like lazy genes. This is

    kind of like that. So you you are kind of like that. So you you are kind of like
    that. So you you are

    actually like this is going to give you actually like this is going to give you
    actually like this is going to give you

    some some some

    basically the reasoning is because at basically the reasoning is because at basically
    the reasoning is because at

    test time we have to sample from Z. So test time we have to sample from Z. So
    test time we have to sample from Z. So

    we cannot we do not have a sampler for we cannot we do not have a sampler for
    we cannot we do not have a sampler for

    X. Actually we''re trying to learn a X. Actually we''re trying to learn a X. Actually
    we''re trying to learn a

    sampler from X. So if you try to be like sampler from X. So if you try to be like
    sampler from X. So if you try to be like

    if you have a onetoone mapping between Z if you have a onetoone mapping between
    Z if you have a onetoone mapping between Z

    and X then like then if you already have and X then like then if you already have
    and X then like then if you already have

    a sampler for Z then right it doesn''t a sampler for Z then right it doesn''t
    a sampler for Z then right it doesn''t

    really Yeah. Yeah. Yeah. Okay. But but yeah but like I I guess Okay. But but yeah
    but like I I guess

    the the gene analogy can kind of explain the the gene analogy can kind of explain
    the the gene analogy can kind of explain

    it a little bit. Not really. Okay. it a little bit. Not really. Okay. it a little
    bit. Not really. Okay.

    Uh do do you still have question though? Uh do do you still have question though?
    Uh do do you still have question though?

    How about someone else can explain it to How about someone else can explain it
    to How about someone else can explain it to

    him? Yeah.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 23
  start_sec: 1073.669
  end_sec: 1124.72
  text: 'him? Yeah. him? Yeah.

    >> Oh, okay. Okay. That''s okay. Go ahead. >> Oh, okay. Okay. That''s okay. Go
    ahead. >> Oh, okay. Okay. That''s okay. Go ahead.

    >> Is there variance of the uh the Q >> Is there variance of the uh the Q >> Is
    there variance of the uh the Q

    distribution and the Qition distribution distribution and the Qition distribution
    distribution and the Qition distribution

    and the P distribution? and the P distribution? and the P distribution?

    >> No, >> No, >> No,

    >> it''s the sigma. We not learning this. >> it''s the sigma. We not learning
    this. >> it''s the sigma. We not learning this.

    >> No, we''re not learning the sigma. >> No, we''re not learning the sigma. >>
    No, we''re not learning the sigma.

    >> This is just like a assumption that we >> This is just like a assumption that
    we >> This is just like a assumption that we

    preset. It is not the same. The previous one is It is not the same. The previous
    one is

    the sigma that conditioned on X. It''s the sigma that conditioned on X. It''s
    the sigma that conditioned on X. It''s

    the sigma of of the Z thing. the sigma of of the Z thing. the sigma of of the
    Z thing.

    >> We''re just assuming it and then it''s >> We''re just assuming it and then
    it''s >> We''re just assuming it and then it''s

    kind of part of the the loss function if kind of part of the the loss function
    if kind of part of the the loss function if

    you want and it could be also be part of you want and it could be also be part
    of you want and it could be also be part of

    the sampling but usually people don''t do the sampling but usually people don''t
    do the sampling but usually people don''t do

    that. Yeah. that. Yeah. that. Yeah.

    >> Literally asked this question to last >> Literally asked this question to last
    >> Literally asked this question to last

    night. night. night.

    >> Oh nice. Okay. >> Oh nice. Okay. >> Oh nice. Okay.

    >> Two he explained to me. One is that u if >> Two he explained to me. One is
    that u if'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 24
  start_sec: 1124.72
  end_sec: 1178.88
  text: '>> Two he explained to me. One is that u if

    it is not a dis a distribution progress it is not a dis a distribution progress
    it is not a dis a distribution progress

    take modeling it is a one to one mapping take modeling it is a one to one mapping
    take modeling it is a one to one mapping

    then it breaks the map because you want then it breaks the map because you want
    then it breaks the map because you want

    progressive modeling forward backward progressive modeling forward backward progressive
    modeling forward backward

    and the second reason is that if you and the second reason is that if you and
    the second reason is that if you

    have a one to one mapping then have a one to one mapping then have a one to one
    mapping then

    uh my guessing is that it''s not really uh my guessing is that it''s not really
    uh my guessing is that it''s not really

    generated because you''ll be mapping one generated because you''ll be mapping
    one generated because you''ll be mapping one

    to one only what''s already in the data to one only what''s already in the data
    to one only what''s already in the data

    and later on if you sample something and later on if you sample something and
    later on if you sample something

    that doesn''t occur in the data. I mean that doesn''t occur in the data. I mean
    that doesn''t occur in the data. I mean

    it''s probably it''s probably it''s probably

    like a whole you end up Yeah. So it ends like a whole you end up Yeah. So it ends
    like a whole you end up Yeah. So it ends

    up being discrete like instead of actual up being discrete like instead of actual
    up being discrete like instead of actual

    >> oh I think it''s variation. >> oh I think it''s variation. >> oh I think it''s
    variation.

    >> Yeah. And also it''s variational right so >> Yeah. And also it''s variational
    right so >> Yeah. And also it''s variational right so

    it''s an approximation. Okay. Cool. But good question. All Okay. Cool. But good
    question. All

    righty. Okay. righty. Okay. righty. Okay.

    Also, by the way, they''re like this is Also, by the way, they''re like this is'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 25
  start_sec: 1178.88
  end_sec: 1228.31
  text: 'Also, by the way, they''re like this is

    like VAE is not the only way to do like VAE is not the only way to do like VAE
    is not the only way to do

    latent variable like and and actually latent variable like and and actually latent
    variable like and and actually

    we''re going to talk about another latent we''re going to talk about another latent
    we''re going to talk about another latent

    variable model today. What that is? All variable model today. What that is? All
    variable model today. What that is? All

    right. Anyway, uh so uh how do you right. Anyway, uh so uh how do you right. Anyway,
    uh so uh how do you

    actually train a VAE, right? Uh actually train a VAE, right? Uh actually train
    a VAE, right? Uh

    basically how you do it in your training basically how you do it in your training
    basically how you do it in your training

    uh loop is that for every existing data uh loop is that for every existing data
    uh loop is that for every existing data

    uh you first encode uh the x and to get uh you first encode uh the x and to get
    uh you first encode uh the x and to get

    your uh mean and variance like that your uh mean and variance like that your uh
    mean and variance like that

    that''s predicted by the encoder. So this that''s predicted by the encoder. So
    this that''s predicted by the encoder. So this

    variance is encoder only. It''s not like variance is encoder only. It''s not like
    variance is encoder only. It''s not like

    related to decoder. And then you sample related to decoder. And then you sample
    related to decoder. And then you sample

    a vector from the standard Gaussian and a vector from the standard Gaussian and
    a vector from the standard Gaussian and

    then you scale it so that you can get then you scale it so that you can get then
    you scale it so that you can get

    your quoteunquote latent uh or your your quoteunquote latent uh or your your quoteunquote
    latent uh or your

    corresponding latent and then you corresponding latent and then you corresponding
    latent and then you

    calculate uh the elbow loss and then you'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 26
  start_sec: 1228.31
  end_sec: 1275.59
  text: 'calculate uh the elbow loss and then you calculate uh the elbow loss and
    then you

    uh optimize it. This is how you train a uh optimize it. This is how you train
    a uh optimize it. This is how you train a

    VAE and then how you sample from a VAE VAE and then how you sample from a VAE
    VAE and then how you sample from a VAE

    is you literally just sample from a from is you literally just sample from a from
    is you literally just sample from a from

    the prior which is standard gausian and the prior which is standard gausian and
    the prior which is standard gausian and

    then you decode it and that''s it. then you decode it and that''s it. then you
    decode it and that''s it.

    So it''s super simple. So it''s super simple. So it''s super simple.

    Okay. But now that we have learned so Okay. But now that we have learned so Okay.
    But now that we have learned so

    many uh gen models, we can sort of like many uh gen models, we can sort of like
    many uh gen models, we can sort of like

    categorize them into two different categorize them into two different categorize
    them into two different

    categories. So the first one is what we categories. So the first one is what we
    categories. So the first one is what we

    call a likelihood bait the model which call a likelihood bait the model which
    call a likelihood bait the model which

    is basically like you''re trying to is basically like you''re trying to is basically
    like you''re trying to

    optimize for the likelihood of the optimize for the likelihood of the optimize
    for the likelihood of the

    existing data by uh like many ways existing data by uh like many ways existing
    data by uh like many ways

    either chain rule or like um like uh uh either chain rule or like um like uh uh
    either chain rule or like um like uh uh

    elbows and stuff like that. And then elbows and stuff like that. And then elbows
    and stuff like that. And then

    there''s two other models that we didn''t there''s two other models that we didn''t
    there''s two other models that we didn''t

    talk about but like they they''re also'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 27
  start_sec: 1275.59
  end_sec: 1327.83
  text: 'talk about but like they they''re also talk about but like they they''re
    also

    likelihood based and we can also do a likelihood based and we can also do a likelihood
    based and we can also do a

    likelihood free way of um modeling the likelihood free way of um modeling the
    likelihood free way of um modeling the

    the the data distribution and the one the the data distribution and the one the
    the data distribution and the one

    that we have seen is called GAN right. that we have seen is called GAN right.
    that we have seen is called GAN right.

    All right. So basically in general um All right. So basically in general um All
    right. So basically in general um

    these models all have the same sort of these models all have the same sort of
    these models all have the same sort of

    like underlying philosophy where like like underlying philosophy where like like
    underlying philosophy where like

    basically our goal is to try to sample basically our goal is to try to sample
    basically our goal is to try to sample

    from this super complicated distribution from this super complicated distribution
    from this super complicated distribution

    like real image but sampling directly like real image but sampling directly like
    real image but sampling directly

    from this like target distribution is from this like target distribution is from
    this like target distribution is

    really difficult uh because they''re really difficult uh because they''re really
    difficult uh because they''re

    complicated and high dimensional and complicated and high dimensional and complicated
    and high dimensional and

    everything. So instead what we do is we everything. So instead what we do is we
    everything. So instead what we do is we

    first sample from a simpler distribution first sample from a simpler distribution
    first sample from a simpler distribution

    such as a a gausian uh and then we just such as a a gausian uh and then we just
    such as a a gausian uh and then we just

    learn a model to sort of like transform learn a model to sort of like transform
    learn a model to sort of like transform

    a sample or this simple distribution a sample or this simple distribution a sample
    or this simple distribution

    into a more complicated one. So this is'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 28
  start_sec: 1327.83
  end_sec: 1403.44
  text: 'into a more complicated one. So this is into a more complicated one. So this
    is

    like sort of like the general underlying like sort of like the general underlying
    like sort of like the general underlying

    philosophy of what these oh these models philosophy of what these oh these models
    philosophy of what these oh these models

    do. All right. But are they are they are do. All right. But are they are they
    are do. All right. But are they are they are

    they all perfect? is that this is like they all perfect? is that this is like
    they all perfect? is that this is like

    you know do they do they are they you know do they do they are they you know do
    they do they are they

    perfect at solving things now what is perfect at solving things now what is perfect
    at solving things now what is

    going on like do they have their own going on like do they have their own going
    on like do they have their own

    flaws uh why don''t we take uh five flaws uh why don''t we take uh five flaws
    uh why don''t we take uh five

    minute go chat with your neighbor say minute go chat with your neighbor say minute
    go chat with your neighbor say

    hello introduce yourself and then talk hello introduce yourself and then talk
    hello introduce yourself and then talk

    about uh what are are they all perfect about uh what are are they all perfect
    about uh what are are they all perfect

    what kind of like drawbacks do they have what kind of like drawbacks do they have
    what kind of like drawbacks do they have

    and uh yeah and by and uh yeah and by and uh yeah and by

    5:30 I''m gonna query randomly from the 5:30 I''m gonna query randomly from the
    5:30 I''m gonna query randomly from the

    audience and uh for each model. How audience and uh for each model. How audience
    and uh for each model. How

    about that? Let''s do that. All right, about that? Let''s do that. All right,
    about that? Let''s do that. All right,

    start talking, man. This It''s 5:30. Now, let let''s start quering It''s 5:30.
    Now, let let''s start quering

    from the from from the audience. from the from from the audience.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 29
  start_sec: 1403.44
  end_sec: 1454.72
  text: 'from the from from the audience.

    H this column. Hello, guys. H Which one H this column. Hello, guys. H Which one
    H this column. Hello, guys. H Which one

    do you prefer? I''ll let you guys pick. do you prefer? I''ll let you guys pick.
    do you prefer? I''ll let you guys pick.

    >> All right. >> All right. >> All right.

    >> Oh, wait. >> Oh, wait. >> Oh, wait.

    >> All right. Never mind. Someone raised >> All right. Never mind. Someone raised
    >> All right. Never mind. Someone raised

    their hand. Hello. I prefer generally their hand. Hello. I prefer generally their
    hand. Hello. I prefer generally

    the VAE training with them. They are the VAE training with them. They are the
    VAE training with them. They are

    more controllable, easier to actually more controllable, easier to actually more
    controllable, easier to actually

    get the outcome that you''re trying to get the outcome that you''re trying to
    get the outcome that you''re trying to

    get. Whereas GANs are difficult to tune get. Whereas GANs are difficult to tune
    get. Whereas GANs are difficult to tune

    despite the fact that like cycle gans despite the fact that like cycle gans despite
    the fact that like cycle gans

    and various things can fit the exact and various things can fit the exact and
    various things can fit the exact

    sample that you''re trying to get to much sample that you''re trying to get to
    much sample that you''re trying to get to much

    much better with a higher likelihood much better with a higher likelihood much
    better with a higher likelihood

    despite not following that Gaussian, despite not following that Gaussian, despite
    not following that Gaussian,

    >> but the gains are generally difficult to >> but the gains are generally difficult
    to >> but the gains are generally difficult to

    really nail. really nail. really nail.

    >> Right. Right. Yeah. Okay. Great. Great. >> Right. Right. Yeah. Okay. Great.
    Great. >> Right. Right. Yeah. Okay. Great. Great.

    Great. So, so, so this is uh what''s your Great. So, so, so this is uh what''s
    your Great. So, so, so this is uh what''s your

    name? name? name?

    >> Johnson. >> Johnson. >> Johnson.

    >> Johnson. >> Johnson.

    >> Okay. So, like, uh, yeah. So, for Gans, >> Okay. So, like, uh, yeah. So, for
    Gans,'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 30
  start_sec: 1454.72
  end_sec: 1510.159
  text: '>> Okay. So, like, uh, yeah. So, for Gans,

    it''s very difficult to train, right? it''s very difficult to train, right? it''s
    very difficult to train, right?

    Basically, that''s what you said. Basically, that''s what you said. Basically,
    that''s what you said.

    >> Yes. Great answer. Great answer. Uh, >> Yes. Great answer. Great answer. Uh,
    >> Yes. Great answer. Great answer. Uh,

    we''re gonna we''re gonna take a look at we''re gonna we''re gonna take a look
    at we''re gonna we''re gonna take a look at

    them like afterwards later. All right. them like afterwards later. All right.
    them like afterwards later. All right.

    Uh, this Wow, this is a large section. Uh, this Wow, this is a large section.
    Uh, this Wow, this is a large section.

    Does anyone want to volunteer? You have Does anyone want to volunteer? You have
    Does anyone want to volunteer? You have

    two more options. Sorry about those two more options. Sorry about those two more
    options. Sorry about those

    people, but uh, yeah, anyone volunteer? people, but uh, yeah, anyone volunteer?
    people, but uh, yeah, anyone volunteer?

    All right. All right. All right.

    >> So, what I imagineed end up end up

    not really a distribution at all. I mean not really a distribution at all. I mean
    not really a distribution at all. I mean

    >> they are actually learning talk about it >> they are actually learning talk
    about it >> they are actually learning talk about it

    but it''s fine. Yeah. but it''s fine. Yeah. but it''s fine. Yeah.

    >> Well too but like it''s not a like it''s >> Well too but like it''s not a like
    it''s >> Well too but like it''s not a like it''s

    not a distribution that like follows any not a distribution that like follows
    any not a distribution that like follows any

    continuous like it doesn''t have the lat space. the lat space.

    >> I see. So basically what you''re saying >> I see. So basically what you''re
    saying >> I see. So basically what you''re saying

    is that they do not actually have a is that they do not actually have a is that
    they do not actually have a

    likelihood basically is that what you''re likelihood basically is that what you''re
    likelihood basically is that what you''re

    saying right like they cannot saying right like they cannot'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 31
  start_sec: 1510.159
  end_sec: 1557.43
  text: 'saying right like they cannot

    >> you like basically is kind of a >> you like basically is kind of a >> you like
    basically is kind of a

    continuous continuous continuous

    >> um so for g for for GANs especially they >> um so for g for for GANs especially
    they >> um so for g for for GANs especially they

    actually have basically they''re uh actually have basically they''re uh actually
    have basically they''re uh

    they''re actually trying to sort of they''re actually trying to sort of they''re
    actually trying to sort of

    optimize for something called Jans and optimize for something called Jans and
    optimize for something called Jans and

    Shannon divergence and that''s actually Shannon divergence and that''s actually
    Shannon divergence and that''s actually

    also a provis divergence so in that also a provis divergence so in that also a
    provis divergence so in that

    sense it''s actually fine. sense it''s actually fine. sense it''s actually fine.

    Yeah, Yeah, Yeah,

    >> I see. >> I see. >> I see.

    >> Yeah, but I I didn''t have time to talk >> Yeah, but I I didn''t have time
    to talk >> Yeah, but I I didn''t have time to talk

    about it. But but yeah, but but like for about it. But but yeah, but but like
    for about it. But but yeah, but but like for

    GAN, another thing that GAN doesn''t do GAN, another thing that GAN doesn''t do
    GAN, another thing that GAN doesn''t do

    well or at all is that you lost access well or at all is that you lost access
    well or at all is that you lost access

    completely to density estimation, right? completely to density estimation, right?
    completely to density estimation, right?

    So you cannot have a likelihood anymore. So you cannot have a likelihood anymore.
    So you cannot have a likelihood anymore.

    All right, someone else in this column All right, someone else in this column
    All right, someone else in this column

    we talk about two games problems. Anyone we talk about two games problems. Anyone
    we talk about two games problems. Anyone

    want to get done on other models? Yes. want to get done on other models? Yes.
    want to get done on other models? Yes.

    >> Uh VAES are going to kind of take the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 32
  start_sec: 1557.43
  end_sec: 1621.83
  text: '>> Uh VAES are going to kind of take the >> Uh VAES are going to kind of
    take the

    average of a distribution because average of a distribution because average of
    a distribution because

    they''re enforcing objection patterns. they''re enforcing objection patterns.
    they''re enforcing objection patterns.

    >> Very good. Very good. Yes. So, VAEs are >> Very good. Very good. Yes. So, VAEs
    are >> Very good. Very good. Yes. So, VAEs are

    going to have sort of like average going to have sort of like average going to
    have sort of like average

    generations, right? Yeah. Yeah. Yeah. generations, right? Yeah. Yeah. Yeah. generations,
    right? Yeah. Yeah. Yeah.

    That''s that''s a great answer. Uh, okay. That''s that''s a great answer. Uh,
    okay. That''s that''s a great answer. Uh, okay.

    Auto reggressive model. Dong Kong LM. Auto reggressive model. Dong Kong LM. Auto
    reggressive model. Dong Kong LM.

    All right. >> I think I brought the pixel. >> I think I brought the pixel.

    >> Yeah. What happens? Not all problems can be Not all problems can be

    especially like based problems. If especially like based problems. If especially
    like based problems. If

    you''re trying to generate a pixel pixel you''re trying to generate a pixel pixel
    you''re trying to generate a pixel pixel

    >> I mean the local properties are >> I mean the local properties are >> I mean
    the local properties are

    consistent but in terms of consistent but in terms of consistent but in terms
    of

    like generating one pixel >> exactly very exactly correct okay so >> exactly very
    exactly correct okay so

    yeah let''s together um what''s wrong with yeah let''s together um what''s wrong
    with yeah let''s together um what''s wrong with

    the previous model right so for auto the previous model right so for auto the
    previous model right so for auto

    reggressive that''s exactly correct reggressive that''s exactly correct reggressive
    that''s exactly correct

    basically in order for you to break basically in order for you to break basically
    in order for you to break

    everything down into chain rules uh you everything down into chain rules uh you
    everything down into chain rules uh you

    will need to basically like you need to will need to basically like you need to
    will need to basically like you need to

    be able to calculate stuff one by one'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 33
  start_sec: 1621.83
  end_sec: 1655.269
  text: 'be able to calculate stuff one by one be able to calculate stuff one by one

    and for text that''s okay because text is and for text that''s okay because text
    is and for text that''s okay because text is

    sequential right so you could like do sequential right so you could like do sequential
    right so you could like do

    you have a good ordering for that but you have a good ordering for that but you
    have a good ordering for that but

    then for image that''s actually then for image that''s actually then for image
    that''s actually

    non-trivial right so like you if you non-trivial right so like you if you non-trivial
    right so like you if you

    want to just like go line by line it want to just like go line by line it want
    to just like go line by line it

    doesn''t make sense anymore right because doesn''t make sense anymore right because
    doesn''t make sense anymore right because

    this is not how you look at a an image this is not how you look at a an image
    this is not how you look at a an image

    you don''t look at an image line by line you don''t look at an image line by line
    you don''t look at an image line by line

    you look at an image as like a general you look at an image as like a general
    you look at an image as like a general

    thing and then you should have like thing and then you should have like thing
    and then you should have like

    patches like you you need to have local patches like you you need to have local
    patches like you you need to have local

    features you need to have a global features you need to have a global features
    you need to have a global

    features you don''t really look at images features you don''t really look at images
    features you don''t really look at images

    line by line. Um and then the second line by line. Um and then the second line
    by line. Um and then the second

    thing is that basically if you need to thing is that basically if you need to
    thing is that basically if you need to

    break things up that everything is going'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 34
  start_sec: 1655.269
  end_sec: 1697.919
  text: 'break things up that everything is going break things up that everything
    is going

    to be really really slow, right? So say to be really really slow, right? So say
    to be really really slow, right? So say

    if you if if let''s suppose you have a if you if if let''s suppose you have a
    if you if if let''s suppose you have a

    like a model autoresent model that that like a model autoresent model that that
    like a model autoresent model that that

    goes pixel by pixel like it calculates goes pixel by pixel like it calculates
    goes pixel by pixel like it calculates

    things really well but even then right things really well but even then right
    things really well but even then right

    if you try to do like say high if you try to do like say high if you try to do
    like say high

    resolution image that just gonna be resolution image that just gonna be resolution
    image that just gonna be

    really painful right because you need to really painful right because you need
    to really painful right because you need to

    like process um the the image pixel by like process um the the image pixel by
    like process um the the image pixel by

    pixel or patch by patch if you do a 4K pixel or patch by patch if you do a 4K
    pixel or patch by patch if you do a 4K

    image that''s like what like like like 8 image that''s like what like like like
    8 image that''s like what like like like 8

    million something four passes of your million something four passes of your million
    something four passes of your

    model and that''s just like crazy. You''re model and that''s just like crazy.
    You''re model and that''s just like crazy. You''re

    just never going to get it done. Okay, just never going to get it done. Okay,
    just never going to get it done. Okay,

    cool. And then for VAE, this is like cool. And then for VAE, this is like cool.
    And then for VAE, this is like

    exactly correct. So VAEs like people exactly correct. So VAEs like people exactly
    correct. So VAEs like people

    from Reddit seven years ago are like why from Reddit seven years ago are like
    why'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 35
  start_sec: 1697.919
  end_sec: 1745.039
  text: 'from Reddit seven years ago are like why

    are VA so blurry? Yeah, that''s because are VA so blurry? Yeah, that''s because
    are VA so blurry? Yeah, that''s because

    uh you know uh vaes are exactly right uh you know uh vaes are exactly right uh
    you know uh vaes are exactly right

    that like they they sort of like learns that like they they sort of like learns
    that like they they sort of like learns

    the average generation a little bit the average generation a little bit the average
    generation a little bit

    because think about it right if you''re because think about it right if you''re
    because think about it right if you''re

    encoder encoder encoder

    learns them to map two different data learns them to map two different data learns
    them to map two different data

    two different data points onto the same two different data points onto the same
    two different data points onto the same

    Z or even even if they''re really close Z or even even if they''re really close
    Z or even even if they''re really close

    to each other which it definitely to each other which it definitely to each other
    which it definitely

    happens right because and nowhere in the happens right because and nowhere in
    the happens right because and nowhere in the

    VAE formulation that you will enforce VAE formulation that you will enforce VAE
    formulation that you will enforce

    this distinction then like you sort of this distinction then like you sort of
    this distinction then like you sort of

    just like that then basically when you just like that then basically when you
    just like that then basically when you

    try to generate from the Z different try to generate from the Z different try
    to generate from the Z different

    fish features of the X is going to pull fish features of the X is going to pull
    fish features of the X is going to pull

    the distribution everywhere and then you the distribution everywhere and then
    you the distribution everywhere and then you

    just kind of ended up generating the just kind of ended up generating the just
    kind of ended up generating the

    average uh data all the time and GANs average uh data all the time and GANs'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 36
  start_sec: 1745.039
  end_sec: 1788.07
  text: 'average uh data all the time and GANs

    are extremely extremely difficult to are extremely extremely difficult to are
    extremely extremely difficult to

    train. Uh, so even though it works train. Uh, so even though it works train. Uh,
    so even though it works

    really well and it was popular, really really well and it was popular, really
    really well and it was popular, really

    popular for like five years, like solid, popular for like five years, like solid,
    popular for like five years, like solid,

    but like man like I don''t know like I''ve but like man like I don''t know like
    I''ve but like man like I don''t know like I''ve

    trained GANs. It''s uh crazy difficult to trained GANs. It''s uh crazy difficult
    to trained GANs. It''s uh crazy difficult to

    train basically like your your loss train basically like your your loss train
    basically like your your loss

    function kind of just like look like function kind of just like look like function
    kind of just like look like

    this and it''s a it''s not really this and it''s a it''s not really this and it''s
    a it''s not really

    basically you actually need to tune your basically you actually need to tune your
    basically you actually need to tune your

    schedules in in terms of like how many schedules in in terms of like how many
    schedules in in terms of like how many

    times do I update my generator, how many times do I update my generator, how many
    times do I update my generator, how many

    times do I update my discriminator, times do I update my discriminator, times
    do I update my discriminator,

    right? Like what is the good dynamic right? Like what is the good dynamic right?
    Like what is the good dynamic

    here? it''s like just really difficult to here? it''s like just really difficult
    to here? it''s like just really difficult to

    train and also if it it''s not well train and also if it it''s not well train
    and also if it it''s not well

    trained or if you do not apply enough trained or if you do not apply enough trained
    or if you do not apply enough

    tricks uh it actually suffers from tricks uh it actually suffers from tricks uh
    it actually suffers from

    something called mode collapse which'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 37
  start_sec: 1788.07
  end_sec: 1833.919
  text: 'something called mode collapse which something called mode collapse which

    just means that like basically it''s sort just means that like basically it''s
    sort just means that like basically it''s sort

    of like reward hacking where the of like reward hacking where the of like reward
    hacking where the

    generator figured out that oh the generator figured out that oh the generator
    figured out that oh the

    discriminator has a problem discriminator has a problem discriminator has a problem

    distinguishing this particular kind of distinguishing this particular kind of
    distinguishing this particular kind of

    image from real image. So instead of image from real image. So instead of image
    from real image. So instead of

    generating diverse image, it''s just generating diverse image, it''s just generating
    diverse image, it''s just

    going to reward hack the distri going to reward hack the distri going to reward
    hack the distri

    discriminator. So they''re just discriminator. So they''re just discriminator.
    So they''re just

    generating the same image all the time generating the same image all the time
    generating the same image all the time

    and then the discriminator just like and then the discriminator just like and
    then the discriminator just like

    would not be able to tell right because would not be able to tell right because
    would not be able to tell right because

    discriminator learned that oh this is I discriminator learned that oh this is
    I discriminator learned that oh this is I

    guess this is real. So it''s just like guess this is real. So it''s just like
    guess this is real. So it''s just like

    all the same image all the time. Okay, all the same image all the time. Okay,
    all the same image all the time. Okay,

    so the previous models are not perfect, so the previous models are not perfect,
    so the previous models are not perfect,

    let''s just say, but let''s just go back let''s just say, but let''s just go back
    let''s just say, but let''s just go back

    to uh their shared strategy, whether to uh their shared strategy, whether to uh
    their shared strategy, whether

    it''s GAN or VAE. The strategy is usually it''s GAN or VAE. The strategy is usually
    it''s GAN or VAE. The strategy is usually

    you sample a noise from a noise you sample a noise from a noise'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 38
  start_sec: 1833.919
  end_sec: 1874.549
  text: 'you sample a noise from a noise

    distribution like Gausian and then you distribution like Gausian and then you
    distribution like Gausian and then you

    apply some sort of like magical training apply some sort of like magical training
    apply some sort of like magical training

    stuff or whatever and then you get a stuff or whatever and then you get a stuff
    or whatever and then you get a

    clean image. This is like your goal, clean image. This is like your goal, clean
    image. This is like your goal,

    right? But this thing is like really right? But this thing is like really right?
    But this thing is like really

    really difficult if you think about it, really difficult if you think about it,
    really difficult if you think about it,

    right? You''re just like just what what right? You''re just like just what what
    right? You''re just like just what what

    what is going on? Like just really what is going on? Like just really what is
    going on? Like just really

    difficult things to do. That''s why difficult things to do. That''s why difficult
    things to do. That''s why

    they''re all imperfect. Um but what if I they''re all imperfect. Um but what if
    I they''re all imperfect. Um but what if I

    tell you your goal now is not to tell you your goal now is not to tell you your
    goal now is not to

    directly go from noise to data. But to directly go from noise to data. But to
    directly go from noise to data. But to

    go from a slightly noisier version of go from a slightly noisier version of go
    from a slightly noisier version of

    the data like you can still see most of the data like you can still see most of
    the data like you can still see most of

    things. It just has some gausian noise things. It just has some gausian noise
    things. It just has some gausian noise

    on it and then you you just go from on it and then you you just go from on it
    and then you you just go from

    there to a clean data. Can you do that? there to a clean data. Can you do that?
    there to a clean data. Can you do that?

    Do you think that''s easier? Yes, it is'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 39
  start_sec: 1874.549
  end_sec: 1921.83
  text: 'Do you think that''s easier? Yes, it is Do you think that''s easier? Yes,
    it is

    easier. This is a healthier type of easier. This is a healthier type of easier.
    This is a healthier type of

    magic. It''s not dark magic anymore. magic. It''s not dark magic anymore. magic.
    It''s not dark magic anymore.

    Okay. Um, so yeah. So one one does not Okay. Um, so yeah. So one one does not
    Okay. Um, so yeah. So one one does not

    simply turn noise into data. I don''t simply turn noise into data. I don''t simply
    turn noise into data. I don''t

    know if you guys still watch Lord of the know if you guys still watch Lord of
    the know if you guys still watch Lord of the

    Rings. Never mind. It''s okay. Rings. Never mind. It''s okay. Rings. Never mind.
    It''s okay.

    I''m old. Anyhow, anyhow. So, so, so like I''m old. Anyhow, anyhow. So, so, so
    like I''m old. Anyhow, anyhow. So, so, so like

    so what if what if we designed the model so what if what if we designed the model
    so what if what if we designed the model

    where we build the training uh uh where we build the training uh uh where we build
    the training uh uh

    supervision by taking the data first supervision by taking the data first supervision
    by taking the data first

    gradually add noise to your training gradually add noise to your training gradually
    add noise to your training

    data and then just like take many many data and then just like take many many
    data and then just like take many many

    steps to to to to add your um noise to steps to to to to add your um noise to
    steps to to to to add your um noise to

    your data. Eventually it reaches the the your data. Eventually it reaches the
    the your data. Eventually it reaches the the

    the complete noise distribution gausian the complete noise distribution gausian
    the complete noise distribution gausian

    and then at training time what we do and then at training time what we do and
    then at training time what we do

    with this data that we constructed is with this data that we constructed is with
    this data that we constructed is

    that we take from a complete noise and'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 40
  start_sec: 1921.83
  end_sec: 1959.519
  text: 'that we take from a complete noise and that we take from a complete noise
    and

    then we gradually try to dn noiseise it then we gradually try to dn noiseise it
    then we gradually try to dn noiseise it

    so that so that at the end it becomes a so that so that at the end it becomes
    a so that so that at the end it becomes a

    clean data. How about we do that? Right? clean data. How about we do that? Right?
    clean data. How about we do that? Right?

    So we just like break it up. We break up So we just like break it up. We break
    up So we just like break it up. We break up

    a very very difficult problem into many a very very difficult problem into many
    a very very difficult problem into many

    many many simpler problems. Right? So many many simpler problems. Right? So many
    many simpler problems. Right? So

    this is diffusion. Now you have a this is diffusion. Now you have a this is diffusion.
    Now you have a

    diffusion model. Class is over. So you diffusion model. Class is over. So you
    diffusion model. Class is over. So you

    have a diffusion. Now this is pretty have a diffusion. Now this is pretty have
    a diffusion. Now this is pretty

    much it. If if if you want to if you much it. If if if you want to if you much
    it. If if if you want to if you

    need to remember anything from this need to remember anything from this need to
    remember anything from this

    lecture, remember this. This is lecture, remember this. This is lecture, remember
    this. This is

    diffusion. Okay. diffusion. Okay. diffusion. Okay.

    Now how how does it work? Okay. From now Now how how does it work? Okay. From
    now Now how how does it work? Okay. From now

    on we''re going to see a lot of math, but on we''re going to see a lot of math,
    but on we''re going to see a lot of math, but

    do not be intimidated. This is uh this do not be intimidated. This is uh this
    do not be intimidated. This is uh this

    is this is all makes sense. All gonna is this is all makes sense. All gonna'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 41
  start_sec: 1959.519
  end_sec: 2003.679
  text: 'is this is all makes sense. All gonna

    make sense. We we just just just channel make sense. We we just just just channel
    make sense. We we just just just channel

    your inner gausian and everything''s your inner gausian and everything''s your
    inner gausian and everything''s

    going to be fine. Okay. This is I going to be fine. Okay. This is I going to be
    fine. Okay. This is I

    promise. All right. Uh so basically this promise. All right. Uh so basically this
    promise. All right. Uh so basically this

    is how we''re going to uh this is how is how we''re going to uh this is how is
    how we''re going to uh this is how

    we''re going to model our our this this we''re going to model our our this this
    we''re going to model our our this this

    forward backward process using math. So forward backward process using math. So
    forward backward process using math. So

    what we do is we call the adding noise what we do is we call the adding noise
    what we do is we call the adding noise

    process a forward process where you just process a forward process where you just
    process a forward process where you just

    literally literally literally

    uh basically the the next sample that uh basically the the next sample that uh
    basically the the next sample that

    you get in your time step is a gausian you get in your time step is a gausian
    you get in your time step is a gausian

    distribution that is related to your distribution that is related to your distribution
    that is related to your

    previous time step uh sample and you add previous time step uh sample and you
    add previous time step uh sample and you add

    some gausian noise to it. Okay, the some gausian noise to it. Okay, the some gausian
    noise to it. Okay, the

    scaled version of your previous um time scaled version of your previous um time
    scaled version of your previous um time

    set. Why does it need to be scaled? set. Why does it need to be scaled? set. Why
    does it need to be scaled?

    We''re going to talk about it or or like We''re going to talk about it or or like'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 42
  start_sec: 2003.679
  end_sec: 2050.0
  text: 'We''re going to talk about it or or like

    does it actually need to be scaled? does it actually need to be scaled? does it
    actually need to be scaled?

    We''re going to talk about it next class. We''re going to talk about it next class.
    We''re going to talk about it next class.

    Okay, not this class, just next class. Okay, not this class, just next class.
    Okay, not this class, just next class.

    Okay, and then the reverse process which Okay, and then the reverse process which
    Okay, and then the reverse process which

    is going from uh going from the left to is going from uh going from the left to
    is going from uh going from the left to

    the right. Okay, so this is the right. Okay, so this is the right. Okay, so this
    is

    uh this is this is what we call the uh this is this is what we call the uh this
    is this is what we call the

    dnoising process, the reverse process. dnoising process, the reverse process.
    dnoising process, the reverse process.

    So we know that we know that the for So we know that we know that the for So we
    know that we know that the for

    process is gausian, right? So it makes process is gausian, right? So it makes
    process is gausian, right? So it makes

    sense for sorry. So it makes sense for sense for sorry. So it makes sense for
    sense for sorry. So it makes sense for

    us to also parameterize the reverse us to also parameterize the reverse us to
    also parameterize the reverse

    process as gausians and uh using the you process as gausians and uh using the
    you process as gausians and uh using the you

    know the the techniques that we learned know the the techniques that we learned
    know the the techniques that we learned

    from VAE we can just parameterize we from VAE we can just parameterize we from
    VAE we can just parameterize we

    don''t really need to parameterize like don''t really need to parameterize like
    don''t really need to parameterize like

    randomly we can parameterize this randomly we can parameterize this randomly we
    can parameterize this

    distribution by their mean and their distribution by their mean and their'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 43
  start_sec: 2050.0
  end_sec: 2104.31
  text: 'distribution by their mean and their

    variance right this is basic or or yeah variance right this is basic or or yeah
    variance right this is basic or or yeah

    so this is what''s happening so this is what''s happening so this is what''s happening

    okay and So okay and So okay and So

    uh let''s just take the general uh uh let''s just take the general uh uh let''s
    just take the general uh

    maximum likelihood route from here. We maximum likelihood route from here. We
    maximum likelihood route from here. We

    want to maximize the log likelihood of want to maximize the log likelihood of
    want to maximize the log likelihood of

    x0 which is x0 is the data. Oh by the x0 which is x0 is the data. Oh by the x0
    which is x0 is the data. Oh by the

    way yes uh so a couple of like time step way yes uh so a couple of like time step
    way yes uh so a couple of like time step

    convention here. So going uh so when convention here. So going uh so when convention
    here. So going uh so when

    you''re going forward you are adding time you''re going forward you are adding
    time you''re going forward you are adding time

    step. So starting from time zero you''re step. So starting from time zero you''re
    step. So starting from time zero you''re

    going from time big t. So this is the going from time big t. So this is the going
    from time big t. So this is the

    forward and then backward is you go like forward and then backward is you go like
    forward and then backward is you go like

    decreasing your your time. So you go decreasing your your time. So you go decreasing
    your your time. So you go

    from big t and then you gradually dn from big t and then you gradually dn from
    big t and then you gradually dn

    noiseise into time zero. Okay. All noiseise into time zero. Okay. All noiseise
    into time zero. Okay. All

    right. Yeah. right. Yeah. right. Yeah.

    >> How big is practice? How big is >> How big is practice? How big is >> How big
    is practice? How big is

    >> great question in general? How big is t?'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 44
  start_sec: 2104.31
  end_sec: 2150.72
  text: '>> great question in general? How big is t? >> great question in general?
    How big is t?

    The this later on the the model that The this later on the the model that The
    this later on the the model that

    we''re going to be mainly looking at the we''re going to be mainly looking at
    the we''re going to be mainly looking at the

    one that developed by Berkeley uh they one that developed by Berkeley uh they
    one that developed by Berkeley uh they

    use 10,00 steps. It''s actually really use 10,00 steps. It''s actually really
    use 10,00 steps. It''s actually really

    really slow. If you guys implement this really slow. If you guys implement this
    really slow. If you guys implement this

    really okay anyway uh but you should really okay anyway uh but you should really
    okay anyway uh but you should

    find out yourself anyway uh but yes 1000 find out yourself anyway uh but yes 1000
    find out yourself anyway uh but yes 1000

    step going back and forth uh why does it step going back and forth uh why does
    it step going back and forth uh why does it

    need 1,00 why does it need so many steps need 1,00 why does it need so many steps
    need 1,00 why does it need so many steps

    we''re going to look at it next class as we''re going to look at it next class
    as we''re going to look at it next class as

    well okay uh so basically uh we want well okay uh so basically uh we want well
    okay uh so basically uh we want

    the the the log likelihood at time zero the the the log likelihood at time zero
    the the the log likelihood at time zero

    so x0 is our clean data right so that''s so x0 is our clean data right so that''s
    so x0 is our clean data right so that''s

    why we want the log likelihood there and why we want the log likelihood there
    and why we want the log likelihood there and

    uh So uh So uh So

    are we familiar with this trick? are we familiar with this trick? are we familiar
    with this trick?

    I shall hope so because this is I shall hope so because this is'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 45
  start_sec: 2150.72
  end_sec: 2204.48
  text: 'I shall hope so because this is

    literally the first step that how we literally the first step that how we literally
    the first step that how we

    develop the elbow from VAE as well, develop the elbow from VAE as well, develop
    the elbow from VAE as well,

    right? All right. So you just like take right? All right. So you just like take
    right? All right. So you just like take

    the marginal into the integral of the the marginal into the integral of the the
    marginal into the integral of the

    joint joint joint

    and then and then and then

    you do the greatest mathematical trick you do the greatest mathematical trick
    you do the greatest mathematical trick

    of all time of all time of all time

    by multiplying and dividing by the same by multiplying and dividing by the same
    by multiplying and dividing by the same

    thing. thing. thing.

    Uh, and then you get an expectation. And Uh, and then you get an expectation.
    And Uh, and then you get an expectation. And

    then now what we do? What what do we do? then now what we do? What what do we
    do? then now what we do? What what do we do?

    Jensen. Yes, that''s right. This guy Jensen. Yes, that''s right. This guy Jensen.
    Yes, that''s right. This guy

    Jensen''s. Jensen''s. Jensen''s.

    Yes. You You apply Jensen''s inequality. Yes. You You apply Jensen''s inequality.
    Yes. You You apply Jensen''s inequality.

    And then you get, do I get this? Okay. And then you get, do I get this? Okay.
    And then you get, do I get this? Okay.

    And then you get this. Okay. So now what And then you get this. Okay. So now what
    And then you get this. Okay. So now what

    you do is you start to break things up. you do is you start to break things up.
    you do is you start to break things up.

    So basically, you see how like so here So basically, you see how like so here
    So basically, you see how like so here

    it''s like it''s still a joint. Okay. is a it''s like it''s still a joint. Okay.
    is a it''s like it''s still a joint. Okay. is a

    joint from time zero to time t. So we''re joint from time zero to time t. So we''re'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 46
  start_sec: 2204.48
  end_sec: 2250.64
  text: 'joint from time zero to time t. So we''re

    just going to break things up into just going to break things up into just going
    to break things up into

    things that we know. So first of all, we things that we know. So first of all,
    we things that we know. So first of all, we

    know that at time t at time big t, the know that at time t at time big t, the
    know that at time t at time big t, the

    probability is a gausian, right? It''s probability is a gausian, right? It''s
    probability is a gausian, right? It''s

    it''s something that we know. It''s it''s something that we know. It''s it''s
    something that we know. It''s

    something that we parameterize, something that we parameterize, something that
    we parameterize,

    something that we chose. So we first something that we chose. So we first something
    that we chose. So we first

    break that thing up and then later break that thing up and then later break that
    thing up and then later

    notice that this is a marovian chain. notice that this is a marovian chain. notice
    that this is a marovian chain.

    This is a markoff chain, right? Uh why This is a markoff chain, right? Uh why
    This is a markoff chain, right? Uh why

    this is a marov chain? Can someone tell this is a marov chain? Can someone tell
    this is a marov chain? Can someone tell

    me why this is a mark of chain? >> Yes. >> Yes.

    >> Depends on the previous time. >> Depends on the previous time. >> Depends on
    the previous time.

    >> Exactly. Because the next time step only >> Exactly. Because the next time
    step only >> Exactly. Because the next time step only

    depend on the previous time step. Right. depend on the previous time step. Right.
    depend on the previous time step. Right.

    So this is a mark of chain as a markoff So this is a mark of chain as a markoff
    So this is a mark of chain as a markoff

    chain. The the markoff property is that chain. The the markoff property is that
    chain. The the markoff property is that

    you can turn the join distribution into you can turn the join distribution into'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 47
  start_sec: 2250.64
  end_sec: 2304.96
  text: 'you can turn the join distribution into

    a chain of the the into a chain of like a chain of the the into a chain of like
    a chain of the the into a chain of like

    the your current given the previous the your current given the previous the your
    current given the previous

    step. So that''s why we can break step. So that''s why we can break step. So that''s
    why we can break

    everything up. Okay. And now now that everything up. Okay. And now now that everything
    up. Okay. And now now that

    we''re breaking things up, uh let''s just we''re breaking things up, uh let''s
    just we''re breaking things up, uh let''s just

    um we then we also need to basically um we then we also need to basically um we
    then we also need to basically

    have this like sort of um have this like sort of um have this like sort of um

    uh oh yeah, sorry. And then now that uh oh yeah, sorry. And then now that uh oh
    yeah, sorry. And then now that

    we''re breaking things up, we also can we''re breaking things up, we also can
    we''re breaking things up, we also can

    break another thing up here, which we''re break another thing up here, which we''re
    break another thing up here, which we''re

    going to know why later. going to know why later. going to know why later.

    But basically this is just like single But basically this is just like single
    But basically this is just like single

    out the last term in this summation and out the last term in this summation and
    out the last term in this summation and

    uh we do uh we do uh we do

    the second greatest trick of the of the the second greatest trick of the of the
    the second greatest trick of the of the

    century but actually this is like century but actually this is like century but
    actually this is like

    similar we we do a very high-end version similar we we do a very high-end version
    similar we we do a very high-end version

    of uh of the um basu here and then of uh of the um basu here and then of uh of
    the um basu here and then

    basically we can get basically we can get'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 48
  start_sec: 2304.96
  end_sec: 2362.72
  text: 'basically we can get

    yeah anyway we can turn we can turn this yeah anyway we can turn we can turn this
    yeah anyway we can turn we can turn this

    Q here into a combination of the three Q here into a combination of the three
    Q here into a combination of the three

    Q''s here. Q''s here. Q''s here.

    And why do we want to do that? It''s And why do we want to do that? It''s And
    why do we want to do that? It''s

    because if you think about it, things because if you think about it, things because
    if you think about it, things

    are going to be able to cancel out, get are going to be able to cancel out, get
    are going to be able to cancel out, get

    cancelled out because the the log of cancelled out because the the log of cancelled
    out because the the log of

    something divided by something is equal something divided by something is equal
    something divided by something is equal

    to log of something minus logs that to log of something minus logs that to log
    of something minus logs that

    thing, right? So if you have a sum of thing, right? So if you have a sum of thing,
    right? So if you have a sum of

    like a bunch of things, that just a like a bunch of things, that just a like a
    bunch of things, that just a

    telescoping series, right? Then you just telescoping series, right? Then you just
    telescoping series, right? Then you just

    like cancel a bunch of things out and like cancel a bunch of things out and like
    cancel a bunch of things out and

    then you move things forward and then you move things forward and then you move
    things forward and

    backward and then you''re going to get backward and then you''re going to get
    backward and then you''re going to get

    something like this. something like this. something like this.

    All right. Any question? So basically go from here So basically go from here

    the sum of log of something divided by the sum of log of something divided by
    the sum of log of something divided by

    something is equal to the sum of log of something is equal to the sum of log of'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 49
  start_sec: 2362.72
  end_sec: 2419.03
  text: 'something is equal to the sum of log of

    this thing minus this thing plus this this thing minus this thing plus this this
    thing minus this thing plus this

    thing minus the next thing and then it''s thing minus the next thing and then
    it''s thing minus the next thing and then it''s

    a telescoping series. a telescoping series. a telescoping series.

    All right I shall hope no one has All right I shall hope no one has All right
    I shall hope no one has

    question question question

    all good. Okay cool. So now that we have all good. Okay cool. So now that we have
    all good. Okay cool. So now that we have

    this thing simple simplified, this thing simple simplified, this thing simple
    simplified,

    if you take a good look at it, this is if you take a good look at it, this is
    if you take a good look at it, this is

    actually a bunch of the sum of a bunch actually a bunch of the sum of a bunch
    actually a bunch of the sum of a bunch

    of KL divergence. So just you can ignore of KL divergence. So just you can ignore
    of KL divergence. So just you can ignore

    everything I say from before. Just everything I say from before. Just everything
    I say from before. Just

    remember this if you don''t want to like remember this if you don''t want to like
    remember this if you don''t want to like

    know the details of the derivation. know the details of the derivation. know the
    details of the derivation.

    You''re not going to be using it in in You''re not going to be using it in in
    You''re not going to be using it in in

    homework. It''s just good to know type of homework. It''s just good to know type
    of homework. It''s just good to know type of

    thing. Uh but yeah basically you can thing. Uh but yeah basically you can thing.
    Uh but yeah basically you can

    literally derive literally derive literally derive

    this lower bound variational lower bound this lower bound variational lower bound
    this lower bound variational lower bound

    right into a bunch of KL divergence. right into a bunch of KL divergence. right
    into a bunch of KL divergence.

    Yeah. A plus a plus a reconstruction'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 50
  start_sec: 2419.03
  end_sec: 2482.88
  text: 'Yeah. A plus a plus a reconstruction Yeah. A plus a plus a reconstruction

    laws. laws. laws.

    Do we do we find this familiar? No way we don''t find this familiar. Do No way
    we don''t find this familiar. Do

    we find this familiar? we find this familiar? we find this familiar?

    Okay. What What is What is it? >> Yeah. The elbow, right? Yeah. Yeah. >> Yeah.
    The elbow, right? Yeah. Yeah.

    Yeah. It''s look like an elbow. Uh well, Yeah. It''s look like an elbow. Uh well,
    Yeah. It''s look like an elbow. Uh well,

    basically basically basically

    this whole thing, you know, this whole this whole thing, you know, this whole
    this whole thing, you know, this whole

    chain of chaos thing is elegant. It''s chain of chaos thing is elegant. It''s
    chain of chaos thing is elegant. It''s

    great in theory. It''s a great idea but great in theory. It''s a great idea but
    great in theory. It''s a great idea but

    uh it this is what what what happened in uh it this is what what what happened
    in uh it this is what what what happened in

    in their 20 uh 2015 paper. So this is in their 20 uh 2015 paper. So this is in
    their 20 uh 2015 paper. So this is

    the this is like the result from the the this is like the result from the the
    this is like the result from the

    original diffusion paper and what we original diffusion paper and what we original
    diffusion paper and what we

    derived just now was they they had from derived just now was they they had from
    derived just now was they they had from

    the 2015 diffusion paper. This is the the 2015 diffusion paper. This is the the
    2015 diffusion paper. This is the

    original the OG. Okay. Uh original the OG. Okay. Uh original the OG. Okay. Uh

    yeah, this is why GAN was famous and yeah, this is why GAN was famous and yeah,
    this is why GAN was famous and

    popular for five years, you know, popular for five years, you know, popular for
    five years, you know,

    doesn''t work that well. Uh so is is doesn''t work that well. Uh so is is'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 51
  start_sec: 2482.88
  end_sec: 2534.88
  text: 'doesn''t work that well. Uh so is is

    there any way that we can make this work there any way that we can make this work
    there any way that we can make this work

    because that whole thing is just too because that whole thing is just too because
    that whole thing is just too

    complicated. Uh well, does anyone have complicated. Uh well, does anyone have
    complicated. Uh well, does anyone have

    any idea just like simple brainstorming any idea just like simple brainstorming
    any idea just like simple brainstorming

    idea? Yes. idea? Yes. idea? Yes.

    >> Number >> Number >> Number

    >> reduce the number of steps. That sounded >> reduce the number of steps. That
    sounded >> reduce the number of steps. That sounded

    like a hyperparameter tuning thing like a hyperparameter tuning thing like a hyperparameter
    tuning thing

    though. Is there any way that like we though. Is there any way that like we though.
    Is there any way that like we

    can fundamentally change things do you can fundamentally change things do you
    can fundamentally change things do you

    think? think? think?

    >> No. >> No. >> No.

    >> No. >> No.

    We''re we''re doomed. This is what''s We''re we''re doomed. This is what''s We''re
    we''re doomed. This is what''s

    happening. Yeah. happening. Yeah. happening. Yeah.

    >> Learning target simplify learning >> Learning target simplify learning >> Learning
    target simplify learning

    target. Okay. How would you do that? target. Okay. How would you do that? target.
    Okay. How would you do that?

    >> Just just look at how you do this. >> Just just look at how you do this. >>
    Just just look at how you do this.

    >> Just train the model to just predict the >> Just train the model to just predict
    the >> Just train the model to just predict the

    loss. Sorry, the the error rating step loss. Sorry, the the error rating step
    loss. Sorry, the the error rating step

    instead of the instead of the instead of the

    >> Yeah, very good. Very good. This is >> Yeah, very good. Very good. This is
    >> Yeah, very good. Very good. This is

    pretty much that. Okay, so we know this pretty much that. Okay, so we know this
    pretty much that. Okay, so we know this

    thing is Markoff, right? Which means thing is Markoff, right? Which means'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 52
  start_sec: 2534.88
  end_sec: 2585.67
  text: 'thing is Markoff, right? Which means

    that at each step, it just adds a very that at each step, it just adds a very
    that at each step, it just adds a very

    small amount of noise to the previous small amount of noise to the previous small
    amount of noise to the previous

    step. So, do we really need to learn the step. So, do we really need to learn
    the step. So, do we really need to learn the

    actual mean and the variance of the the actual mean and the variance of the the
    actual mean and the variance of the the

    each gausian distribution? Because this each gausian distribution? Because this
    each gausian distribution? Because this

    these distributions are actually these distributions are actually these distributions
    are actually

    extremely complicated, right? It''s a extremely complicated, right? It''s a extremely
    complicated, right? It''s a

    combination of a very complicated combination of a very complicated combination
    of a very complicated

    distribution, the the the image plus distribution, the the the image plus distribution,
    the the the image plus

    some noise. It''s like just oh what it''s some noise. It''s like just oh what
    it''s some noise. It''s like just oh what it''s

    really really difficult to learn right really really difficult to learn right
    really really difficult to learn right

    but do we really need to learn this but do we really need to learn this but do
    we really need to learn this

    difficult distribution no right because difficult distribution no right because
    difficult distribution no right because

    we know that we is just adding noise we know that we is just adding noise we know
    that we is just adding noise

    then why don''t we just learn a dino then why don''t we just learn a dino then
    why don''t we just learn a dino

    noiser that can predict the noise right noiser that can predict the noise right
    noiser that can predict the noise right

    and then we just reduce the noise like and then we just reduce the noise like
    and then we just reduce the noise like

    gradually at every time step right why gradually at every time step right why
    gradually at every time step right why

    can''t we just do that can''t we just do that can''t we just do that

    uh uh uh

    you absolutely could now you have ddpm'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 53
  start_sec: 2585.67
  end_sec: 2630.069
  text: 'you absolutely could now you have ddpm you absolutely could now you have
    ddpm

    so if you if if there''s another slide so if you if if there''s another slide
    so if you if if there''s another slide

    that you want to remember from today. that you want to remember from today. that
    you want to remember from today.

    This is the slide that you should This is the slide that you should This is the
    slide that you should

    remember. This is literally DDPM. remember. This is literally DDPM. remember.
    This is literally DDPM.

    All right. All right.

    Cool. So, how a lot of math again. A lot Cool. So, how a lot of math again. A
    lot Cool. So, how a lot of math again. A lot

    of math again. Buckle up. Okay. So, how of math again. Buckle up. Okay. So, how
    of math again. Buckle up. Okay. So, how

    do we derive DDPM from from from the do we derive DDPM from from from the do we
    derive DDPM from from from the

    from the math? All right. from the math? All right. from the math? All right.

    Let''s just like think about what kind of Let''s just like think about what kind
    of Let''s just like think about what kind of

    designs that we can simplify from here. designs that we can simplify from here.
    designs that we can simplify from here.

    So first of all we should definitely fix So first of all we should definitely
    fix So first of all we should definitely fix

    the forward process right because like the forward process right because like
    the forward process right because like

    we know it''s just adding noise and we we know it''s just adding noise and we
    we know it''s just adding noise and we

    should we should be able to know what should we should be able to know what should
    we should be able to know what

    how much noise that is is adding because how much noise that is is adding because
    how much noise that is is adding because

    like we we we should be able to choose like we we we should be able to choose
    like we we we should be able to choose

    it so we just fix it right we just have'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 54
  start_sec: 2630.069
  end_sec: 2678.4
  text: 'it so we just fix it right we just have it so we just fix it right we just
    have

    a fixed noising schedule that each time a fixed noising schedule that each time
    a fixed noising schedule that each time

    step we know how like what gausian that step we know how like what gausian that
    step we know how like what gausian that

    we''re adding noise that the what gausian we''re adding noise that the what gausian
    we''re adding noise that the what gausian

    noise that we''re adding to the the noise that we''re adding to the the noise
    that we''re adding to the the

    previous step right so mathematically previous step right so mathematically previous
    step right so mathematically

    this is basically just saying that Like this is basically just saying that Like
    this is basically just saying that Like

    first of all this is a marovian chain first of all this is a marovian chain first
    of all this is a marovian chain

    and then uh each uh at each step this is and then uh each uh at each step this
    is and then uh each uh at each step this is

    a gausian distribution that is dependent a gausian distribution that is dependent
    a gausian distribution that is dependent

    on the previous step and then all of on the previous step and then all of on the
    previous step and then all of

    these beta things are prefix so we chose these beta things are prefix so we chose
    these beta things are prefix so we chose

    them ahead of time these are not them ahead of time these are not them ahead of
    time these are not

    learned. All right. So to make things learned. All right. So to make things learned.
    All right. So to make things

    easier, basically they just um easier, basically they just um easier, basically
    they just um

    they if if you if you calculate they if if you if you calculate they if if you
    if you calculate

    basically if you um because one gausian basically if you um because one gausian
    basically if you um because one gausian

    plus another gausian is a third gausian, plus another gausian is a third gausian,
    plus another gausian is a third gausian,

    right? So one gausian plus another right? So one gausian plus another'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 55
  start_sec: 2678.4
  end_sec: 2724.15
  text: 'right? So one gausian plus another

    gausian plus t gausian is still a gausian plus t gausian is still a gausian plus
    t gausian is still a

    gausian. So instead of like at in the gausian. So instead of like at in the gausian.
    So instead of like at in the

    forward process instead of actually just forward process instead of actually just
    forward process instead of actually just

    like gradually add a bunch of noise you like gradually add a bunch of noise you
    like gradually add a bunch of noise you

    can actually just directly compute what can actually just directly compute what
    can actually just directly compute what

    is your noise level at time t from your is your noise level at time t from your
    is your noise level at time t from your

    clean data right and that''s just as long clean data right and that''s just as
    long clean data right and that''s just as long

    as you know what t you''re going to uh as you know what t you''re going to uh
    as you know what t you''re going to uh

    because because you can just like you because because you can just like you because
    because you can just like you

    know yeah so that''s that''s very that''s know yeah so that''s that''s very that''s
    know yeah so that''s that''s very that''s

    very nice that''s very easy so now we very nice that''s very easy so now we very
    nice that''s very easy so now we

    have like a one step four process for have like a one step four process for have
    like a one step four process for

    every single time step right that''s every single time step right that''s every
    single time step right that''s

    Uh the second thing that is nice about Uh the second thing that is nice about
    Uh the second thing that is nice about

    this is that this thing the first item this is that this thing the first item
    this is that this thing the first item

    now it''s a constant. It doesn''t really now it''s a constant. It doesn''t really
    now it''s a constant. It doesn''t really

    mean anything anymore because we choose mean anything anymore because we choose
    mean anything anymore because we choose

    both Q and P to be the same gausian. So'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 56
  start_sec: 2724.15
  end_sec: 2776.24
  text: 'both Q and P to be the same gausian. So both Q and P to be the same gausian.
    So

    it''s it''s going to be perfect every it''s it''s going to be perfect every it''s
    it''s going to be perfect every

    time. Doesn''t matter. We don''t need to time. Doesn''t matter. We don''t need
    to time. Doesn''t matter. We don''t need to

    learn it anymore. learn it anymore. learn it anymore.

    All right. And uh because we have this All right. And uh because we have this
    All right. And uh because we have this

    because we have this like one step like because we have this like one step like
    because we have this like one step like

    one step jump forward of the forward one step jump forward of the forward one
    step jump forward of the forward

    process. Uh we can also like process. Uh we can also like process. Uh we can also
    like

    look at how in the second part right in look at how in the second part right in
    look at how in the second part right in

    sec second part here we need this like sec second part here we need this like
    sec second part here we need this like

    weird conditional forward process that weird conditional forward process that
    weird conditional forward process that

    conditioned on zero and on x0. Um conditioned on zero and on x0. Um conditioned
    on zero and on x0. Um

    basically we you can also just like basically we you can also just like basically
    we you can also just like

    sorry you can also just like write this sorry you can also just like write this
    sorry you can also just like write this

    out out out

    as a function of xt and x0 zero and it as a function of xt and x0 zero and it
    as a function of xt and x0 zero and it

    is going to be like and and and it''s is going to be like and and and it''s is
    going to be like and and and it''s

    going to be like closed form. So we also going to be like closed form. So we also
    going to be like closed form. So we also

    know in closed form the mean and the know in closed form the mean and the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 57
  start_sec: 2776.24
  end_sec: 2820.48
  text: 'know in closed form the mean and the

    variance of this particular uh uh variance of this particular uh uh variance of
    this particular uh uh

    distribution that we''re going to use. distribution that we''re going to use.
    distribution that we''re going to use.

    Okay, cool. We''re getting close. We''re Okay, cool. We''re getting close. We''re
    Okay, cool. We''re getting close. We''re

    getting close. I promise we''re getting getting close. I promise we''re getting
    getting close. I promise we''re getting

    close. So, now we fixed this part. We close. So, now we fixed this part. We close.
    So, now we fixed this part. We

    fixed this part. You guys see that fixed this part. You guys see that fixed this
    part. You guys see that

    person? person? person?

    >> Yeah, we fixed this part. So, now we >> Yeah, we fixed this part. So, now we
    >> Yeah, we fixed this part. So, now we

    need to deal with the P part. We now now need to deal with the P part. We now
    now need to deal with the P part. We now now

    we need to deal with the thing that we need to deal with the thing that we need
    to deal with the thing that

    we''re actually learning. Okay. we''re actually learning. Okay. we''re actually
    learning. Okay.

    So in order to make things easier to So in order to make things easier to So in
    order to make things easier to

    learn, they actually found that in real learn, they actually found that in real
    learn, they actually found that in real

    life, if you fix the variance of the life, if you fix the variance of the life,
    if you fix the variance of the

    reverse process and only learn the reverse process and only learn the reverse
    process and only learn the

    means, it works just fine. It works means, it works just fine. It works means,
    it works just fine. It works

    really well. It doesn''t matter. And really well. It doesn''t matter. And really
    well. It doesn''t matter. And

    there are two ways to to to um to define there are two ways to to to um to define
    there are two ways to to to um to define

    this this variance based on the variance this this variance based on the variance'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 58
  start_sec: 2820.48
  end_sec: 2873.67
  text: 'this this variance based on the variance

    that you choose for the forward process. that you choose for the forward process.
    that you choose for the forward process.

    But basically what we can do is we can But basically what we can do is we can
    But basically what we can do is we can

    literally just uh fix the variance here literally just uh fix the variance here
    literally just uh fix the variance here

    and only learn the mean. So now we we and only learn the mean. So now we we and
    only learn the mean. So now we we

    have a very very very simple uh have a very very very simple uh have a very very
    very simple uh

    objective. We only learn the mean of the objective. We only learn the mean of
    the objective. We only learn the mean of the

    gausians in the forward proc in the gausians in the forward proc in the gausians
    in the forward proc in the

    backward process. Right? And the backward process. Right? And the backward process.
    Right? And the

    reminder this is a reminder that we can reminder this is a reminder that we can
    reminder this is a reminder that we can

    we can do this. Um we can do this. Um we can do this. Um

    so that just brings us to basically now so that just brings us to basically now
    so that just brings us to basically now

    we have a KL of two gausians again right we have a KL of two gausians again right
    we have a KL of two gausians again right

    and that just like basically brings us and that just like basically brings us
    and that just like basically brings us

    the very very simplified form of each the very very simplified form of each the
    very very simplified form of each

    time step in the middle right so this is time step in the middle right so this
    is time step in the middle right so this is

    the loss of the time step in in the the loss of the time step in in the the loss
    of the time step in in the

    middle it''s literally just an L2 between middle it''s literally just an L2 between
    middle it''s literally just an L2 between

    this mean versus the mean that you'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 59
  start_sec: 2873.67
  end_sec: 2928.8
  text: 'this mean versus the mean that you this mean versus the mean that you

    predict Any predict Any predict Any

    question? Nope. Alrighty. Nope. Alrighty.

    All right. Now we have everything. All right. Now we have everything. All right.
    Now we have everything.

    Bear with me. Bear with me. Now we have Bear with me. Bear with me. Now we have
    Bear with me. Bear with me. Now we have

    everything. We channel the the trick everything. We channel the the trick everything.
    We channel the the trick

    that we just learned today. The that we just learned today. The that we just learned
    today. The

    reparameterization trick. So if you look reparameterization trick. So if you look
    reparameterization trick. So if you look

    at it, right? If you look at it, this is at it, right? If you look at it, this
    is at it, right? If you look at it, this is

    the one step forward that we have. We the one step forward that we have. We the
    one step forward that we have. We

    know that this is happening. So we can know that this is happening. So we can
    know that this is happening. So we can

    so we know that you can literally so we know that you can literally so we know
    that you can literally

    express XT in terms of the X0 express XT in terms of the X0 express XT in terms
    of the X0

    and the and and and and the epsilon that and the and and and and the epsilon that
    and the and and and and the epsilon that

    it generates. So basically you can break it generates. So basically you can break
    it generates. So basically you can break

    up a noisy sample into the sample part up a noisy sample into the sample part
    up a noisy sample into the sample part

    and the noise part basically that''s what and the noise part basically that''s
    what and the noise part basically that''s what

    they say that''s what that''s what they''re they say that''s what that''s what
    they''re they say that''s what that''s what they''re

    saying and you know exactly how much saying and you know exactly how much saying
    and you know exactly how much

    weight you should give to each based on weight you should give to each based on'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 60
  start_sec: 2928.8
  end_sec: 2988.63
  text: 'weight you should give to each based on

    your your your time step. So this is the your your your time step. So this is
    the your your your time step. So this is the

    reparameter same reparameterization reparameter same reparameterization reparameter
    same reparameterization

    trick. You you break things up into your trick. You you break things up into your
    trick. You you break things up into your

    mean and variance essentially. And mean and variance essentially. And mean and
    variance essentially. And

    now that we have this, bear with me. Now now that we have this, bear with me.
    Now now that we have this, bear with me. Now

    that we have this, then we can literally that we have this, then we can literally
    that we have this, then we can literally

    plug in the x0 part, right? So basically plug in the x0 part, right? So basically
    plug in the x0 part, right? So basically

    you just move things around. You will you just move things around. You will you
    just move things around. You will

    get an expression that sorry, you''ll get get an expression that sorry, you''ll
    get get an expression that sorry, you''ll get

    an expression that an expression that an expression that

    that fits the x0. This this second that fits the x0. This this second that fits
    the x0. This this second

    argument here is your x0 from your argument here is your x0 from your argument
    here is your x0 from your

    reparameterization trick. Nobody''s confused. All right. Good. Nobody''s confused.
    All right. Good.

    Good. Good. Very good. Very good. And Good. Good. Very good. Very good. And Good.
    Good. Very good. Very good. And

    then we channel some high-end bayas then we channel some high-end bayas then we
    channel some high-end bayas

    theorem again. And then you ended up theorem again. And then you ended up theorem
    again. And then you ended up

    basically you just like plug everything basically you just like plug everything
    basically you just like plug everything

    in and then do some algebra and then in and then do some algebra and then in and
    then do some algebra and then

    you''re going to get something like this. you''re going to get something like
    this. you''re going to get something like this.

    Okay. Okay. Okay.

    Why is this a good thing you may ask?'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 61
  start_sec: 2988.63
  end_sec: 3054.72
  text: 'Why is this a good thing you may ask? Why is this a good thing you may ask?

    This is so complicated. Why do we want This is so complicated. Why do we want
    This is so complicated. Why do we want

    this? It is because this? It is because this? It is because

    this part reminder. So this part is a this part reminder. So this part is a this
    part reminder. So this part is a

    mean, right? This part is a mean and mean, right? This part is a mean and mean,
    right? This part is a mean and

    you can do reparameterization. Anyway, basically you can do Anyway, basically
    you can do

    reparameterization again and then reparameterization again and then reparameterization
    again and then

    basically this thing is just telling you basically this thing is just telling
    you basically this thing is just telling you

    that like you can you don''t really need that like you can you don''t really need
    that like you can you don''t really need

    to learn the mean because to learn the mean because to learn the mean because

    like like the x0 is represented like like the x0 is represented like like the
    x0 is represented

    let so the xt can be represented by the let so the xt can be represented by the
    let so the xt can be represented by the

    noise part and the data part. Similarly, noise part and the data part. Similarly,
    noise part and the data part. Similarly,

    the data can be represented by the noise the data can be represented by the noise
    the data can be represented by the noise

    and the noisy data. So, basically, you and the noisy data. So, basically, you
    and the noisy data. So, basically, you

    just shift things around and then you''re just shift things around and then you''re
    just shift things around and then you''re

    going to be able to get a sort of like going to be able to get a sort of like
    going to be able to get a sort of like

    a x a noisy data plus noise version a x a noisy data plus noise version a x a
    noisy data plus noise version

    uh of your that that can represent your uh of your that that can represent your'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 62
  start_sec: 3054.72
  end_sec: 3110.0
  text: 'uh of your that that can represent your

    prediction. And then here is why you can prediction. And then here is why you
    can prediction. And then here is why you can

    directly predict the noise. All right. directly predict the noise. All right.
    directly predict the noise. All right.

    So all of this is to try to say we can So all of this is to try to say we can
    So all of this is to try to say we can

    directly predict the noise and train a directly predict the noise and train a
    directly predict the noise and train a

    dinoiser. All right. It doesn''t really dinoiser. All right. It doesn''t really
    dinoiser. All right. It doesn''t really

    Yeah. Okay. That''s does is everyone Yeah. Okay. That''s does is everyone Yeah.
    Okay. That''s does is everyone

    clear about what''s happening here? clear about what''s happening here? clear
    about what''s happening here?

    Do we have confusion? Do we do do we Do we have confusion? Do we do do we Do we
    have confusion? Do we do do we

    have questions? All right. Anyway, so like the full All right. Anyway, so like
    the full

    story is that you you channel some Baya story is that you you channel some Baya
    story is that you you channel some Baya

    theorem, you channel some theorem, you channel some theorem, you channel some

    reparameterization trick, you channel reparameterization trick, you channel reparameterization
    trick, you channel

    multiple times uh and then you you you multiple times uh and then you you you
    multiple times uh and then you you you

    you rearrange things and then you apply you rearrange things and then you apply
    you rearrange things and then you apply

    some algebra and then you will be able some algebra and then you will be able
    some algebra and then you will be able

    to get the uh the elbow or the to get the uh the elbow or the to get the uh the
    elbow or the

    variational vari uh lower bound is variational vari uh lower bound is variational
    vari uh lower bound is

    equivalent to training a dinoiser which equivalent to training a dinoiser which
    equivalent to training a dinoiser which

    literally they simplify into a L2 loss literally they simplify into a L2 loss'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 63
  start_sec: 3110.0
  end_sec: 3164.79
  text: 'literally they simplify into a L2 loss

    between the the noise that you''re adding between the the noise that you''re adding
    between the the noise that you''re adding

    to your sample and the predicted noise to your sample and the predicted noise
    to your sample and the predicted noise

    that you''re having from this is your XT that you''re having from this is your
    XT that you''re having from this is your XT

    right from your XT from a noisy sample right from your XT from a noisy sample
    right from your XT from a noisy sample

    and your time stamp. So literally it''s a and your time stamp. So literally it''s
    a and your time stamp. So literally it''s a

    L2 loss between the predicted noise and L2 loss between the predicted noise and
    L2 loss between the predicted noise and

    the actual noise. That''s it. the actual noise. That''s it. the actual noise.
    That''s it.

    Okay. I hope I hope this is clear. But Okay. I hope I hope this is clear. But
    Okay. I hope I hope this is clear. But

    now let me know if you have questions. now let me know if you have questions.
    now let me know if you have questions.

    But now you have the EPM training. This But now you have the EPM training. This
    But now you have the EPM training. This

    is very nice. is very nice. is very nice.

    All right. Like All right. Like All right. Like

    slightly slightly more math. Trust the slightly slightly more math. Trust the
    slightly slightly more math. Trust the

    process. Okay. It''s going to be fine. Uh process. Okay. It''s going to be fine.
    Uh process. Okay. It''s going to be fine. Uh

    but basically now that you have this but basically now that you have this but
    basically now that you have this

    um you can also write um you can also write um you can also write

    your next time step in terms of your your next time step in terms of your your
    next time step in terms of your

    previous time step and the noise that previous time step and the noise that previous
    time step and the noise that

    you predicted. Yeah, obviously right you predicted. Yeah, obviously right you
    predicted. Yeah, obviously right

    because the the the noise you predicted'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 64
  start_sec: 3164.79
  end_sec: 3207.119
  text: 'because the the the noise you predicted because the the the noise you predicted

    is literally how much noise should I d is literally how much noise should I d
    is literally how much noise should I d

    noiseise from my uh from my current time noiseise from my uh from my current time
    noiseise from my uh from my current time

    step. And basically if you just scale it step. And basically if you just scale
    it step. And basically if you just scale it

    well enough, you just scale it properly, well enough, you just scale it properly,
    well enough, you just scale it properly,

    you''re gonna be able to get a sample you''re gonna be able to get a sample you''re
    gonna be able to get a sample

    from your uh from the next time step or from your uh from the next time step or
    from your uh from the next time step or

    the previous time step that you''re the previous time step that you''re the previous
    time step that you''re

    trying to sample from that you''re trying trying to sample from that you''re trying
    trying to sample from that you''re trying

    to d noiseise to. Um to d noiseise to. Um to d noiseise to. Um

    yeah, and uh basically just a reminder yeah, and uh basically just a reminder
    yeah, and uh basically just a reminder

    why this is the case is because look at why this is the case is because look at
    why this is the case is because look at

    this uh uh uh uh distribution. So the this uh uh uh uh distribution. So the this
    uh uh uh uh distribution. So the

    distribution that we''re trying to aim distribution that we''re trying to aim
    distribution that we''re trying to aim

    for is this Gaussian that has this for is this Gaussian that has this for is this
    Gaussian that has this

    predicted mean and the fixed variance. predicted mean and the fixed variance.
    predicted mean and the fixed variance.

    So all you need to do is to figure out So all you need to do is to figure out
    So all you need to do is to figure out

    the the the the expression for the the the the the expression for the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 65
  start_sec: 3207.119
  end_sec: 3260.96
  text: 'the the the the expression for the

    predicted mean of that is given by XT. predicted mean of that is given by XT.
    predicted mean of that is given by XT.

    So your previous time your your current So your previous time your your current
    So your previous time your your current

    time step sample and the predicted time step sample and the predicted time step
    sample and the predicted

    noise. Once you figure that out, you noise. Once you figure that out, you noise.
    Once you figure that out, you

    just need to like make it into a gausian just need to like make it into a gausian
    just need to like make it into a gausian

    by adding some noise to it. by adding some noise to it. by adding some noise to
    it.

    Okay. Okay.

    All All good. All good. Yeah. All All good. All good. Yeah. All All good. All
    good. Yeah.

    >> We''re predicting is directly from XT to >> We''re predicting is directly from
    XT to >> We''re predicting is directly from XT to

    X0. X0. X0.

    >> Uh sort of. Yeah. Sort of. Yeah. sort of. Yeah. Sort of. Yeah.

    >> We only move back one time step. >> We only move back one time step. >> We
    only move back one time step.

    >> Yeah. That''s why that''s why you have a >> Yeah. That''s why that''s why you
    have a >> Yeah. That''s why that''s why you have a

    bunch of like terms here, right? That''s bunch of like terms here, right? That''s
    bunch of like terms here, right? That''s

    why you have a bunch of like scaling why you have a bunch of like scaling why
    you have a bunch of like scaling

    here. So that so so so that it''s like here. So that so so so that it''s like
    here. So that so so so that it''s like

    actually basically you are you are still actually basically you are you are still
    actually basically you are you are still

    trying to only get to the the next time trying to only get to the the next time
    trying to only get to the the next time

    step. You''re not trying to jump from to step. You''re not trying to jump from
    to'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 66
  start_sec: 3260.96
  end_sec: 3300.16
  text: 'step. You''re not trying to jump from to

    x0 yet. Uh in order to jump to x0 x0 yet. Uh in order to jump to x0 x0 yet. Uh
    in order to jump to x0

    there''s actually a paper about it. And there''s actually a paper about it. And
    there''s actually a paper about it. And

    then there''s a form you you should be then there''s a form you you should be
    then there''s a form you you should be

    able to derive your formula here. And able to derive your formula here. And able
    to derive your formula here. And

    that thing actually enables you fast that thing actually enables you fast that
    thing actually enables you fast

    sampling. Uh but but basically yeah what sampling. Uh but but basically yeah what
    sampling. Uh but but basically yeah what

    you''re doing here is like you''re still you''re doing here is like you''re still
    you''re doing here is like you''re still

    trying to like basically follow the trying to like basically follow the trying
    to like basically follow the

    distribution that you defined at the distribution that you defined at the distribution
    that you defined at the

    beginning. It''s just that now that we beginning. It''s just that now that we
    beginning. It''s just that now that we

    are parameterizing the model to predict are parameterizing the model to predict
    are parameterizing the model to predict

    the noise, uh how do we get an the noise, uh how do we get an the noise, uh how
    do we get an

    expression from this thing and then we expression from this thing and then we
    expression from this thing and then we

    we''re still trying to uh make a sample we''re still trying to uh make a sample
    we''re still trying to uh make a sample

    from this thing and this is just like from this thing and this is just like from
    this thing and this is just like

    the the thing that you calculated as the the thing that you calculated as the
    the thing that you calculated as

    mean plus the uh the standard deviation mean plus the uh the standard deviation
    mean plus the uh the standard deviation

    plus a gausian noise. So this is still plus a gausian noise. So this is still'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 67
  start_sec: 3300.16
  end_sec: 3353.839
  text: 'plus a gausian noise. So this is still

    this this distribution. Okay, this this distribution. Okay, this this distribution.
    Okay,

    any other questions? Cool. Erh anyhow anyhow so that''s it for Cool. Erh anyhow
    anyhow so that''s it for

    the math today I promise I''m so sorry the math today I promise I''m so sorry
    the math today I promise I''m so sorry

    but you know I hope this is fun and we but you know I hope this is fun and we
    but you know I hope this is fun and we

    get to use so many things that we get to use so many things that we get to use
    so many things that we

    learned from VAE uh but anyway the point learned from VAE uh but anyway the point
    learned from VAE uh but anyway the point

    is the actual algorithm is actually is the actual algorithm is actually is the
    actual algorithm is actually

    super simple right so what you do is you super simple right so what you do is
    you super simple right so what you do is you

    first sample a data distribution from first sample a data distribution from first
    sample a data distribution from

    your data uh sorry sample a data point your data uh sorry sample a data point
    your data uh sorry sample a data point

    from your data distribution and then you from your data distribution and then
    you from your data distribution and then you

    sample a time step and then you sample a time step and then you sample a time
    step and then you

    basically just uh do one step forward basically just uh do one step forward basically
    just uh do one step forward

    jumping. Yeah. So you get a an XT from jumping. Yeah. So you get a an XT from
    jumping. Yeah. So you get a an XT from

    your data and the noise that you sampled your data and the noise that you sampled
    your data and the noise that you sampled

    uh and then you predict the noise and uh and then you predict the noise and uh
    and then you predict the noise and

    then you try to like basically see if then you try to like basically see if'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 68
  start_sec: 3353.839
  end_sec: 3391.99
  text: 'then you try to like basically see if

    the noise that you predict is accurate the noise that you predict is accurate
    the noise that you predict is accurate

    uh in comparison to the the ground truth uh in comparison to the the ground truth
    uh in comparison to the the ground truth

    that you just sampled. Uh and that''s it. that you just sampled. Uh and that''s
    it. that you just sampled. Uh and that''s it.

    And then you just train it this way. And then you just train it this way. And
    then you just train it this way.

    Super easy. Super easy. Super easy.

    Uh and then for the for the sampling Uh and then for the for the sampling Uh and
    then for the for the sampling

    it''s also very easy. It''s basically just it''s also very easy. It''s basically
    just it''s also very easy. It''s basically just

    you start from complete noise. So you you start from complete noise. So you you
    start from complete noise. So you

    sample a gausian and then for each time sample a gausian and then for each time
    sample a gausian and then for each time

    step you literally just do what we did. step you literally just do what we did.
    step you literally just do what we did.

    You you figure out like basically how You you figure out like basically how You
    you figure out like basically how

    much noise you want to d noiseise and much noise you want to d noiseise and much
    noise you want to d noiseise and

    then you scale it properly so that you then you scale it properly so that you
    then you scale it properly so that you

    actually get the mean that you intend to actually get the mean that you intend
    to actually get the mean that you intend to

    get and then you make it into a gausian get and then you make it into a gausian
    get and then you make it into a gausian

    a sample from the correct gausian. And a sample from the correct gausian. And
    a sample from the correct gausian. And

    then you just do that for every steps. then you just do that for every steps.
    then you just do that for every steps.

    And then like 10,000 steps later, you'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 69
  start_sec: 3391.99
  end_sec: 3445.44
  text: 'And then like 10,000 steps later, you And then like 10,000 steps later, you

    get a sample. Make sense? Make sense?

    Cool. Amazing. And and the model is Cool. Amazing. And and the model is Cool.
    Amazing. And and the model is

    amazing, too. Look at that. This is what amazing, too. Look at that. This is what
    amazing, too. Look at that. This is what

    killed Gan kind of. Well, Gan is not killed Gan kind of. Well, Gan is not killed
    Gan kind of. Well, Gan is not

    completely dead, but you know, you see completely dead, but you know, you see
    completely dead, but you know, you see

    this is like people at the time was like this is like people at the time was like
    this is like people at the time was like

    amazed that this is this is like amazed that this is this is like amazed that
    this is this is like

    incredible pro progress from five years incredible pro progress from five years
    incredible pro progress from five years

    ago, right? this thing really works ago, right? this thing really works ago, right?
    this thing really works

    really really well. And uh another thing really really well. And uh another thing
    really really well. And uh another thing

    to mention that now I feel like we to mention that now I feel like we to mention
    that now I feel like we

    should probably have a sense now but should probably have a sense now but should
    probably have a sense now but

    diffusion models are kind of like just diffusion models are kind of like just
    diffusion models are kind of like just

    va right. So if you think about it uh we va right. So if you think about it uh
    we va right. So if you think about it uh we

    are trying to first map a clean data are trying to first map a clean data are
    trying to first map a clean data

    with whatever process that we have into with whatever process that we have into
    with whatever process that we have into

    some like gausian noise or some gausian some like gausian noise or some gausian
    some like gausian noise or some gausian

    latent let''s just say and then later latent let''s just say and then later'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 70
  start_sec: 3445.44
  end_sec: 3498.24
  text: 'latent let''s just say and then later

    we''re trying to map this latent this we''re trying to map this latent this we''re
    trying to map this latent this

    gausian uh into the a reconstruction of gausian uh into the a reconstruction of
    gausian uh into the a reconstruction of

    the data again right so if you think the data again right so if you think the
    data again right so if you think

    about it this is literally just a very about it this is literally just a very
    about it this is literally just a very

    very deep very long va right where you very deep very long va right where you
    very deep very long va right where you

    where but like the only trick here is where but like the only trick here is where
    but like the only trick here is

    that the encoder is not learned it''s that the encoder is not learned it''s that
    the encoder is not learned it''s

    completely fixed and the only thing that completely fixed and the only thing that
    completely fixed and the only thing that

    you''re learning is your decoder and then you''re learning is your decoder and
    then you''re learning is your decoder and then

    you basically just like okay now I have you basically just like okay now I have
    you basically just like okay now I have

    this like fixed way to encode my data this like fixed way to encode my data this
    like fixed way to encode my data

    into this latent kind of like how do I into this latent kind of like how do I
    into this latent kind of like how do I

    recover my data like the only thing you recover my data like the only thing you
    recover my data like the only thing you

    you this is the only thing you care you this is the only thing you care you this
    is the only thing you care

    about now so yeah so diffusion models about now so yeah so diffusion models about
    now so yeah so diffusion models

    are lowkey VAEEs or highkey VAE actually are lowkey VAEEs or highkey VAE actually
    are lowkey VAEEs or highkey VAE actually

    um yeah >> in this case C doesn''t really depend on >> in this case C doesn''t
    really depend on

    X X'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 71
  start_sec: 3498.24
  end_sec: 3552.549
  text: 'X

    >> no >> no >> no

    >> well well basically it doesn''t depend on X in well basically it doesn''t depend
    on X in

    the sense that it''s not like the sense that it''s not like the sense that it''s
    not like

    it doesn''t it it does not depend on like it doesn''t it it does not depend on
    like it doesn''t it it does not depend on like

    basically like you should like because a basically like you should like because
    a basically like you should like because a

    gausian is a gausian right a gausian is gausian is a gausian right a gausian is
    gausian is a gausian right a gausian is

    the random distribution it shouldn''t the random distribution it shouldn''t the
    random distribution it shouldn''t

    really associate with the like some dog really associate with the like some dog
    really associate with the like some dog

    pictures but in this case it it is it is pictures but in this case it it is it
    is pictures but in this case it it is it is

    related because this is learned so related because this is learned so related
    because this is learned so

    basically at sampling time your latent basically at sampling time your latent
    basically at sampling time your latent

    your Z your noise is still going to sort your Z your noise is still going to sort
    your Z your noise is still going to sort

    of determine like what you''re going to of determine like what you''re going to
    of determine like what you''re going to

    generate later it still has a generate later it still has a generate later it
    still has a

    relationship but it doesn''t but relationship but it doesn''t but relationship
    but it doesn''t but

    everything is learned and it''s everything is learned and it''s everything is
    learned and it''s

    associated by your learn the model it''s associated by your learn the model it''s
    associated by your learn the model it''s

    not like you don''t it''s it''s not an not like you don''t it''s it''s not an
    not like you don''t it''s it''s not an

    actual like they don''t actually have a actual like they don''t actually have
    a actual like they don''t actually have a

    relationship but you just sort of relationship but you just sort of relationship
    but you just sort of

    enforced it.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 72
  start_sec: 3555.75
  end_sec: 3602.47
  text: '>> This will be closer to this one like you >> This will be closer to this
    one like you

    can do interpolation which has an can do interpolation which has an can do interpolation
    which has an

    effect. effect. effect.

    Do you think this cannot be Do you think this cannot be Do you think this cannot
    be

    interpolation? interpolation? interpolation?

    >> Interpolation would work. Maybe >> Interpolation would work. Maybe >> Interpolation
    would work. Maybe

    >> why not? Oh, you can try it. Actually, >> why not? Oh, you can try it. Actually,
    >> why not? Oh, you can try it. Actually,

    try it with your learn the model in your try it with your learn the model in your
    try it with your learn the model in your

    homework. Actually, that''s a great idea. homework. Actually, that''s a great
    idea. homework. Actually, that''s a great idea.

    >> Let''s see has any like semantic. >> Let''s see has any like semantic. >> Let''s
    see has any like semantic.

    >> Um, I guess the problem is for VAE, the >> Um, I guess the problem is for VAE,
    the >> Um, I guess the problem is for VAE, the

    quote unquote semantic meanings for the quote unquote semantic meanings for the
    quote unquote semantic meanings for the

    latent space is also kind of like or or latent space is also kind of like or or
    latent space is also kind of like or or

    fake. I mean, not not fake, but it''s fake. I mean, not not fake, but it''s fake.
    I mean, not not fake, but it''s

    like pseudo, right? is like they they like pseudo, right? is like they they like
    pseudo, right? is like they they

    try to make some interpretation out of try to make some interpretation out of
    try to make some interpretation out of

    it. Oh, also another important it. Oh, also another important it. Oh, also another
    important

    distinctions of and maybe that''s why distinctions of and maybe that''s why distinctions
    of and maybe that''s why

    that VAE can enforce more semantics on that VAE can enforce more semantics on
    that VAE can enforce more semantics on

    the latent space is that an actual VA the latent space is that an actual VA the
    latent space is that an actual VA

    should be an autoenccoder which means'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 73
  start_sec: 3602.47
  end_sec: 3644.96
  text: 'should be an autoenccoder which means should be an autoenccoder which means

    that uh it it should have some that uh it it should have some that uh it it should
    have some

    compression actually. So basically the compression actually. So basically the
    compression actually. So basically the

    the the latent space is usually way the the latent space is usually way the the
    latent space is usually way

    smaller dimension and there''s some like smaller dimension and there''s some like
    smaller dimension and there''s some like

    2017 paper that basically just says that 2017 paper that basically just says that
    2017 paper that basically just says that

    oh actually uh the jacobian of the like oh actually uh the jacobian of the like
    oh actually uh the jacobian of the like

    the decoder of of of an autoenccoder the decoder of of of an autoenccoder the
    decoder of of of an autoenccoder

    actually give you access to the manifold actually give you access to the manifold
    actually give you access to the manifold

    of your data. What is a manifold? of your data. What is a manifold? of your data.
    What is a manifold?

    Manifold is basically just like a lower Manifold is basically just like a lower
    Manifold is basically just like a lower

    dimensional representation of your data. dimensional representation of your data.
    dimensional representation of your data.

    So this is why uh if you are doing the So this is why uh if you are doing the
    So this is why uh if you are doing the

    traditional VAEs that you sort of traditional VAEs that you sort of traditional
    VAEs that you sort of

    compressing it, you are actually going compressing it, you are actually going
    compressing it, you are actually going

    to have some semantic meanings because to have some semantic meanings because
    to have some semantic meanings because

    of the the like the incode to a lower of the the like the incode to a lower of
    the the like the incode to a lower

    dimensional space and then uh decode uh dimensional space and then uh decode uh
    dimensional space and then uh decode uh

    operation. But then at diffusion here operation. But then at diffusion here operation.
    But then at diffusion here

    this is not very clear anymore and it''s this is not very clear anymore and it''s'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 74
  start_sec: 3644.96
  end_sec: 3689.28
  text: 'this is not very clear anymore and it''s

    because um it''s like the the noise and because um it''s like the the noise and
    because um it''s like the the noise and

    the data are of the same dimension. So the data are of the same dimension. So
    the data are of the same dimension. So

    it doesn''t necessarily need to can can it doesn''t necessarily need to can can
    it doesn''t necessarily need to can can

    have this uh compression. Yeah. have this uh compression. Yeah. have this uh compression.
    Yeah.

    >> Could you add that? Could you add that >> Could you add that? Could you add
    that >> Could you add that? Could you add that

    paper you just referenced to the paper you just referenced to the paper you just
    referenced to the

    research? research? research?

    >> Yes. Yes, of course. >> Yes. Yes, of course. >> Yes. Yes, of course.

    >> It''s actually a workshop paper or >> It''s actually a workshop paper or >>
    It''s actually a workshop paper or

    something. I think it''s a very short something. I think it''s a very short something.
    I think it''s a very short

    paper, but it''s a great read. Okay. paper, but it''s a great read. Okay. paper,
    but it''s a great read. Okay.

    Anyway, uh Anyway, uh Anyway, uh

    all right. Another thing that you guys all right. Another thing that you guys
    all right. Another thing that you guys

    should pay attention to actually is uh should pay attention to actually is uh
    should pay attention to actually is uh

    what what model architecture right what what model architecture right what what
    model architecture right

    should we use to train a DDPM model? Uh should we use to train a DDPM model? Uh
    should we use to train a DDPM model? Uh

    the DDPM paper use a unit. Uh why is it the DDPM paper use a unit. Uh why is it
    the DDPM paper use a unit. Uh why is it

    called UNET? because it''s a U-shaped called UNET? because it''s a U-shaped called
    UNET? because it''s a U-shaped

    neuronet network. So that''s why it''s neuronet network. So that''s why it''s
    neuronet network. So that''s why it''s

    called a unit. Okay. Uh so exactly what called a unit. Okay. Uh so exactly what'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 75
  start_sec: 3689.28
  end_sec: 3736.16
  text: 'called a unit. Okay. Uh so exactly what

    it is is basically you have some input it is is basically you have some input
    it is is basically you have some input

    like input image right and then you are like input image right and then you are
    like input image right and then you are

    gradually uh downsampling it. So at each gradually uh downsampling it. So at each
    gradually uh downsampling it. So at each

    level level or at each layer you kind of level level or at each layer you kind
    of level level or at each layer you kind of

    just like down or each block I guess just like down or each block I guess just
    like down or each block I guess

    you''re down down sampling it to a low you''re down down sampling it to a low
    you''re down down sampling it to a low

    dimensional enough space and then you do dimensional enough space and then you
    do dimensional enough space and then you do

    some processing in this low dimensional some processing in this low dimensional
    some processing in this low dimensional

    space and do you do upsample again and space and do you do upsample again and
    space and do you do upsample again and

    the key thing in a unit is that the key thing in a unit is that the key thing
    in a unit is that

    you need to have some skip connections you need to have some skip connections
    you need to have some skip connections

    between each sort of like layer of your between each sort of like layer of your
    between each sort of like layer of your

    spatial dimension. And why is that or spatial dimension. And why is that or spatial
    dimension. And why is that or

    why is unit in general good for why is unit in general good for why is unit in
    general good for

    diffusion at least for right now we''re diffusion at least for right now we''re
    diffusion at least for right now we''re

    we''re going to talk about like more we''re going to talk about like more we''re
    going to talk about like more

    advanced architectures later is because advanced architectures later is because
    advanced architectures later is because

    basically you are downsampling and basically you are downsampling and'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 76
  start_sec: 3736.16
  end_sec: 3790.069
  text: 'basically you are downsampling and

    upsampling your uh your image so that upsampling your uh your image so that upsampling
    your uh your image so that

    like basically you sort of covers both like basically you sort of covers both
    like basically you sort of covers both

    the coarse feature and the fine features the coarse feature and the fine features
    the coarse feature and the fine features

    in your model and also the skip in your model and also the skip in your model
    and also the skip

    connection kind of keeps like like um I connection kind of keeps like like um
    I connection kind of keeps like like um I

    guess crucial spatial uh you know guess crucial spatial uh you know guess crucial
    spatial uh you know

    information that is like so that you information that is like so that you information
    that is like so that you

    don''t lose information when you''re don''t lose information when you''re don''t
    lose information when you''re

    downsampling uh and then upsampling downsampling uh and then upsampling downsampling
    uh and then upsampling

    again. And then um the convolution again. And then um the convolution again. And
    then um the convolution

    obviously is a very good inductive bias obviously is a very good inductive bias
    obviously is a very good inductive bias

    for image because it takes care of the for image because it takes care of the
    for image because it takes care of the

    local relationship unlike you know just local relationship unlike you know just
    local relationship unlike you know just

    scan line you know processing and also scan line you know processing and also
    scan line you know processing and also

    it''s like very easy to set up this uh it''s like very easy to set up this uh
    it''s like very easy to set up this uh

    network because it''s this thing is network because it''s this thing is network
    because it''s this thing is

    actually um I believe it is developed actually um I believe it is developed actually
    um I believe it is developed

    for segmentation so like it''s it''s for segmentation so like it''s it''s for
    segmentation so like it''s it''s

    basically designed for uh the situations basically designed for uh the situations
    basically designed for uh the situations

    where input and outputs are about the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 77
  start_sec: 3790.069
  end_sec: 3837.28
  text: 'where input and outputs are about the where input and outputs are about the

    same dimensionality same dimensionality same dimensionality

    um spatially. Uh but basically later on um spatially. Uh but basically later on
    um spatially. Uh but basically later on

    people have some alternatives but UNED people have some alternatives but UNED
    people have some alternatives but UNED

    dominated the diffusion research for the dominated the diffusion research for
    the dominated the diffusion research for the

    beginning two to three years and it''s beginning two to three years and it''s
    beginning two to three years and it''s

    like incredible because this is like a like incredible because this is like a
    like incredible because this is like a

    2015 uh paper. I actually have my lab 2015 uh paper. I actually have my lab 2015
    uh paper. I actually have my lab

    majors like show up at my office today majors like show up at my office today
    majors like show up at my office today

    and he saw me making a UNET uh slide and and he saw me making a UNET uh slide
    and and he saw me making a UNET uh slide and

    he laughed at me. But you know laugh at he laughed at me. But you know laugh at
    he laughed at me. But you know laugh at

    me all you want. This thing dominated me all you want. This thing dominated me
    all you want. This thing dominated

    the fusion for three years. It''s it''s the fusion for three years. It''s it''s
    the fusion for three years. It''s it''s

    good. Okay. Uh the last thing that we''re good. Okay. Uh the last thing that we''re
    good. Okay. Uh the last thing that we''re

    g that I''m gonna talk about uh which g that I''m gonna talk about uh which g
    that I''m gonna talk about uh which

    you''re actually going to be deriving for you''re actually going to be deriving
    for you''re actually going to be deriving for

    your homework. Uh you can also do other your homework. Uh you can also do other
    your homework. Uh you can also do other

    duration. This is one way to do it. But duration. This is one way to do it. But
    duration. This is one way to do it. But

    basically basically

    because because'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 78
  start_sec: 3837.28
  end_sec: 3883.44
  text: 'because

    uh we because we have this like rep like uh we because we have this like rep like
    uh we because we have this like rep like

    this way to represent uh the the noisy this way to represent uh the the noisy
    this way to represent uh the the noisy

    samples, right? So the noisy sample is samples, right? So the noisy sample is
    samples, right? So the noisy sample is

    equal to uh a combination of the clean equal to uh a combination of the clean
    equal to uh a combination of the clean

    sample and the noise and in the original sample and the noise and in the original
    sample and the noise and in the original

    DDP we choose to model the noise part DDP we choose to model the noise part DDP
    we choose to model the noise part

    right right right

    uh equivalently you can also try to uh equivalently you can also try to uh equivalently
    you can also try to

    model the clean part right because there model the clean part right because there
    model the clean part right because there

    are only two parts the clean part and are only two parts the clean part and are
    only two parts the clean part and

    the noise part uh so if you try to model the noise part uh so if you try to model
    the noise part uh so if you try to model

    the clean part then channeling the the clean part then channeling the the clean
    part then channeling the

    previous thing that we have discovered previous thing that we have discovered
    previous thing that we have discovered

    then you can actually write the the the then you can actually write the the the
    then you can actually write the the the

    the mean that we need in the loss the mean that we need in the loss the mean that
    we need in the loss

    function in a very clean way as well. function in a very clean way as well. function
    in a very clean way as well.

    And if you do that then you can And if you do that then you can And if you do
    that then you can

    literally just plug in this thing into literally just plug in this thing into'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 79
  start_sec: 3883.44
  end_sec: 3925.52
  text: 'literally just plug in this thing into

    your mean and then you you should be your mean and then you you should be your
    mean and then you you should be

    able to get a nicely formulated closed able to get a nicely formulated closed
    able to get a nicely formulated closed

    form loss function uh as well. Uh so um form loss function uh as well. Uh so um
    form loss function uh as well. Uh so um

    people later about two years after DPM people later about two years after DPM
    people later about two years after DPM

    also discovered that oh actually you can also discovered that oh actually you
    can also discovered that oh actually you can

    do a combination like you don''t like do a combination like you don''t like do
    a combination like you don''t like

    basically you can either predict the basically you can either predict the basically
    you can either predict the

    noise or predict the clean image but you noise or predict the clean image but
    you noise or predict the clean image but you

    can also try to predict some weird can also try to predict some weird can also
    try to predict some weird

    combination of both and actually that combination of both and actually that combination
    of both and actually that

    thing is the best thing that you can do thing is the best thing that you can do
    thing is the best thing that you can do

    sort of. So it''s like pretty interesting sort of. So it''s like pretty interesting
    sort of. So it''s like pretty interesting

    how people just play around with math. how people just play around with math.
    how people just play around with math.

    Uh anyway, so uh yeah, so now that we''re Uh anyway, so uh yeah, so now that we''re
    Uh anyway, so uh yeah, so now that we''re

    closer to the end of the class, actually closer to the end of the class, actually
    closer to the end of the class, actually

    very close to the end of the class, uh very close to the end of the class, uh
    very close to the end of the class, uh

    we should now know what diffusion model we should now know what diffusion model'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 80
  start_sec: 3925.52
  end_sec: 3966.119
  text: 'we should now know what diffusion model

    is. And in this class, we basically just is. And in this class, we basically just
    is. And in this class, we basically just

    derive the diffusion model from from derive the diffusion model from from derive
    the diffusion model from from

    scratch using a likelihood based method scratch using a likelihood based method
    scratch using a likelihood based method

    just like how we derive the VAE. just like how we derive the VAE. just like how
    we derive the VAE.

    In the next class, however, we''re going In the next class, however, we''re going
    In the next class, however, we''re going

    to be deriving the same diffusion model, to be deriving the same diffusion model,
    to be deriving the same diffusion model,

    but from a completely different but from a completely different but from a completely
    different

    perspective. And this time we do not perspective. And this time we do not perspective.
    And this time we do not

    need to maximize likelihood anymore. And need to maximize likelihood anymore.
    And need to maximize likelihood anymore. And

    we also are gonna be using a new we also are gonna be using a new we also are
    gonna be using a new

    technique that we have never seen technique that we have never seen technique
    that we have never seen

    before. All right. So this is the end of before. All right. So this is the end
    of before. All right. So this is the end of

    the class. Thank you for coming. Uh the class. Thank you for coming. Uh the class.
    Thank you for coming. Uh

    remember to uh you know uh do your remember to uh you know uh do your remember
    to uh you know uh do your

    homework and stuff and hopefully I''ll homework and stuff and hopefully I''ll
    homework and stuff and hopefully I''ll

    see you tomorrow at the guest lecture.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
---
# CMU 10799 S26: Lecture 2 - Denoising Diffusion Models - Diffusion & Flow Matching

See the structured chunks above.
