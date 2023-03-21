package com.ssafy.vitawearable.repo;

import com.ssafy.vitawearable.entity.WeeklyWearable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface WeeklyWearableRepo extends JpaRepository<WeeklyWearable,Long> {
    List<WeeklyWearable> findByUser_UserId(String userId);
}
