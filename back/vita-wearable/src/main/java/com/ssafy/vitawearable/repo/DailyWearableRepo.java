package com.ssafy.vitawearable.repo;

import com.ssafy.vitawearable.entity.DailyWearable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface DailyWearableRepo extends JpaRepository<DailyWearable,Long> {
    // userId로 일일 데이터 리스트를 추출
    List<DailyWearable> findByUser_UserId(String userId);
}
