# Future Plans and Roadmap

## Overview
This document tracks the upcoming features, goals, and architectural plans for the ShareBear application, specifically focusing on the newly implemented user models and referral program.

## 1. Referral Program Implementation
**Goal:** Encourage peer-to-peer sharing by rewarding users after successfully referring a set number of new users.
*   **Actionable Plan:** 
    *   Currently, the `users.User` model tracks `referral_code`, `referred_by`, and `referral_count` dynamically. 
    *   **Phase 2:** Implement logic in the backend (likely in a `post_save` signal or dedicated service layer) that monitors `referral_count`. 
    *   **Phase 3:** Create a system to automatically distribute the "Reward" (e.g., "$10 off first purchase") when `referral_count` reaches `3`. This might involve creating a `Reward` or `DiscountCode` model tied to the User, or an integration with a payment provider like Stripe to apply credits to their account.

## 2. Analytics Integration
**Goal:** Track "Intent" (Buy/Sell/Both) to build analytics for the development team.
*   **Actionable Plan:** 
    *   Create internal admin dashboards or export scripts to analyze the distribution of `FRESHMAN`/`SOPHOMORE`/etc. classifications against their chosen `intent`. 
    *   Use this data to tailor marketing campaigns or balance supply (Sellers) with demand (Buyers).

## 3. UI/UX Dashboard Enhancements
**Goal:** The user dashboard currently does not change based on intent, but it should present the available analytics clearly or seamlessly provide both buying and selling capabilities.
*   **Actionable Plan:** 
    *   In the frontend, continue developing a unified dashboard where users can manage their referrals, view their unique `referral_code`, and see how many signups they have generated.
    *   Expose the user's `username` for display purposes across the app, while enforcing `email` and password for secure login.

## 4. Supabase & Database Stability
**Goal:** Complete the migration to the custom user model.
*   **Actionable Plan:** 
    *   **Immediate Need:** Drop existing migrations from the database, or reset the Supabase instance entirely to allow Django to apply the initial custom user migrations properly.
    *   After resetting, create a superuser for standard admin testing.
